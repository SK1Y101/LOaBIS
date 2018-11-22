import sys, time, os, subprocess
from datetime import datetime

def _elog(err="",say=1):
    _log("Error: "+str(type(err))+"; "+str(err)+"\n")
    if say:
        _say("Software encountered an error, consider submitting log to developers","Error")

def _say(txt="",cli="System"):
    for x in str(cli+": "+txt)+"\n":
        sys.stdout.write(x)
        time.sleep(0.003)

def _log(txt="",say=0):
    y=open("log.txt","a")
    y.write("["+str(datetime.now())+"] - "+txt[0].upper()+txt[1:]+"\n")
    y.close()
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
        _log(str(stype[0])+" modules prevented from loading: "+str(stype[3]),0)
        _say(str(sum(stype[1:3]))+" modules loaded, "+str(stype[0])+" prevented from loading")
        
        for x in getexcept(modinfo,"LOaBIS Core"):
            a=""
            try:
                exec("from "+str(x[0])+" import *")
                a=1
            except Exception as e:
                _log("unknown error, "+str(x[0])+" not loaded",1)
                _elog(e,0)
                modinfo.pop(modinfo.index(x))
            if a:
                yes
                #load all the functions
        interface()

    except Exception as e:
        _elog(e)
