import sys, time, os, subprocess, csv
from datetime import datetime

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
        modinfo=[]
        for x in modules:
            modinfo.append(getinfo(x))
        core=getdat(modinfo,"LOaBIS Core")
        _log(str(core[0])+" v"+str(core[1])+" Loaded",1)
        subprocess.call("title "+str(core[0])+" v"+str(core[1])+" - "+str(core[3]),shell=True)

        stype=[0,0,0,[]]
        _log("Fetching pip modules",1)
        pipmods=getpip()
        _log("Fetching dependancies",1)
        for x in getexcept(modinfo,"LOaBIS Core"):
            tmp=0
            for y in x[6]:
                if getdat(modinfo,y):
                    modinfo=getexcept(modinfo,x)+x
                else:
                    _log(str(y)+" not installed for "+str(x[0]),1)
                    stype[0]+=1
                    tmp+=1
                    break
            for y in x[7]:
                if not getdat(pipmods,y):
                    tmp+=module.inst(y)
            b=simver(core[1],x[2])
            if b:
                stype[b]+=1
            else:
                tmp+=1
            if tmp>0:
                modinfo.pop(modinfo.index(x))
                stype[3].append(x[0])

        _log(str(stype[2])+" stable modules loaded")
        _log(str(stype[1])+" unstable modules loaded")
        _log(str(stype[0])+" modules prevented from loading: "+str(stype[3]))
        _say(str(sum(stype[1:3]))+" modules loaded, "+str(stype[0])+" prevented from loading")
        
        import_start=datetime.now()
        for x in modinfo:
            a=""
            try:
                if x != core:
                    exec("from "+str(x[0])+" import *")
                try:
                    b=[]
                    with open(str(x[0])+sep+"commands.txt","r") as f:
                        for row in csv.reader(f):
                            c=row[0].split(":")[1]
                            module.funcs.append(c)
                            module.cwords.append(str(row[0].split(":")[0]+" ").replace("  "," "))
                            module.desc.append(row[1])
                            b.append(c)
                    _log("Imported functions from "+str(x[0])+"; "+str(b))
                except Exception as e:
                    _elog(e)
            except Exception as e:
                _log("unknown error, "+str(x[0])+" not loaded",1)
                _elog(e,0)
                modinfo.pop(modinfo.index(x))
            if a:
                a=1#yes
                #load all the functions
        module.funcs.append("null")
        module.cwords.append("null")
        module.desc.append("null")
        
        import_time=divmod((datetime.now()-import_start).total_seconds(),60)
        _log("Function initialisation complete, took "+str(import_time[0]*60+import_time[1])+" seconds")

        elapsed_time=divmod((datetime.now()-start_time).total_seconds(),60)
        _log("Startup successfull, took "+str(elapsed_time[0]*60+elapsed_time[1])+" seconds")

        _log("Initialisation complete, loading interface",1)
        interface()

    except Exception as e:
        _elog(e)
