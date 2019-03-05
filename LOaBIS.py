import sys, time, os, subprocess, csv
from datetime import datetime

def execute(func=""):
    for x in func:
        try:
            globals()[str(x)]()
        except Exception as e:
            _elog(e)

def _elog(err="",say=1):
    _log("Error: "+str(type(err))+"; "+str(err))
    if say:
        _say("Software encountered an error, consider submitting log to developers","Error")

def _say(txt="",cli="System"):
    for x in str(cli+": "+txt)+"\n":
        sys.stdout.write(x)
        time.sleep(0.003)

def _log(txt="",say=0):
    with open("log.txt","a") as y:
        y.write("["+str(datetime.now())+"] - "+txt[0].upper()+txt[1:]+"\n")
    if say:
        _say(txt)

if __name__=="__main__":
    try:
        start_time=datetime.now()
        _log("Initialising software",1)
        from _core import *
        from _core import module
        globals()["shutdown"]=False
        avoid=["__pycache__",".git"]
        modules=getexcept(next(os.walk(os.getcwd()))[1],avoid)
        modules.sort()
        _log(str(len(modules))+" Modules located: "+str(modules))

        _log("Loading module data",1)
        modinfo,_mods=[],[]
        for x in modules:
            modinfo.append(getinfo(x))
            _mods.append(getinfo(x))
        core,_mods=getdat(modinfo,"LOaBIS Core"),getexcept(_mods,"LOaBIS Core")
        _log(str(core[0])+" v"+str(core[1])+" Loaded",1)
        subprocess.call("title "+str(core[0])+" v"+str(core[1])+" - "+str(core[3]),shell=True)

        stype=[0,0,0,[],[],[],"prevented","unstable","stable"]
        _log("Fetching pip modules",1)
        pipmods=getpip()
        _log("Fetching dependancies",1)

        for x in _mods:
            tmp=0
            if x[6]:
                for y in x[6]:
                    if not getdat(modinfo,y):
                        _log(str(y)+" not installed for "+str(x[0]),1)
                        stype[0]+=1
                        tmp+=1
                modinfo.append(modinfo.pop(modinfo.index(x)))
            for y in x[7]:
                if not getdat(pipmods,y):
                    tmp+=module.inst(y)
            b=simver(core[1],x[2])
            if b:
                stype[b]+=1
                stype[5-b].append(x[0]+" v"+x[1])
            else:
                tmp+=1
            if tmp>0:
                stype[5].append(x[0]+" v"+x[1])
                modinfo.remove(x)

        for x in range(3):
            _log(str(stype[2-x])+" "+str(stype[8-x])+" modules: "+str(stype[3+x]))
        _say(str(sum(stype[1:3]))+" modules loaded, "+str(stype[0])+" prevented from loading")

        import_start=datetime.now()
        fn=[["sta",0,0],["shu",0,0],["per",0,0],["pst",0,0],["rep",0,0]]
        _log("Importing module functions",1)
        for x in modinfo:
            a,b,d=0,[],[0,0,0,0,0]
            try:
                if x != core:
                    exec("from "+str(x[0])+" import *")
                try:
                    with open(str(x[0])+sep+"commands.txt","r") as f:
                        for row in csv.reader(f):
                            c=row[0].split(":")[1]
                            module.funcs.append(c)
                            module.cwords.append(str(row[0].split(":")[0]+" ").replace("  "," "))
                            module.desc.append(row[1])
                            b.append(c)
                    _log("Imported functions from "+str(x[0])+"; "+str(b))
                    a=1
                except Exception as e:
                    _elog(e)
            except Exception as e:
                _log("unknown error, "+str(x[0])+" not loaded",1)
                _elog(e,0)
                modinfo.pop(modinfo.index(x))
            if a:
                for y in x[8]:
                    module.stafunc.append(y)
                    d[0]+=1
                for y in x[9]:
                    module.endfunc.append(y)
                    d[1]+=1
                for y in x[10]:
                    module.perfunc.append(y)
                    d[2]+=1
                for y in x[11]:
                    module.pstfunc.append(y)
                    d[3]+=1
                for y in x[12]:
                    try:
                        globals()[y[0]]=globals()[y[1]]
                        d[4]+=1
                    except:
                        pass
                for x in range(len(d)):
                    fn[x][1:3]=fn[x][1]+d[x],fn[x][2]+int(bool(d[x]))
        for x in fn:
            if x[1]:
                _log(str(x[1])+" "+str(x[0])+" functions loaded from "+str(x[2])+" modules")
        module.funcs.append("null")
        module.cwords.append("null")
        module.desc.append("null")

        import_time=divmod((datetime.now()-import_start).total_seconds(),60)
        _log("Function initialisation complete, took "+str(import_time[0]*60+import_time[1])+" seconds")

        _log("Executing final procedures",1)
        if module.stafunc:
            _log("Running startup functions",1)
            execute(module.stafunc)
        if module.perfunc or module.pstfunc:
            _log("Running persistence handler")

        elapsed_time=divmod((datetime.now()-start_time).total_seconds(),60)
        _log("Startup successfull, took "+str(elapsed_time[0]*60+elapsed_time[1])+" seconds")

        _log("Initialisation complete, loading interface",1)
        interface()

        if module.endfunc:
            _log("Running shutdown functions",1)
            execute(module.endfunc)

    except Exception as e:
        _elog(e)
