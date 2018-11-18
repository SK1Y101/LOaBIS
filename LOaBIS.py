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
        subprocess.call("title "+str(core[0])+" v"+str(core[1])+" - "+str(core[2]),shell=True)

        stype=[0,0,[]]
        _log("Fetching pip modules (if any)",1)
        pipmods=getpip()
        _log("Fetching dependancies",1)
        for x in getexcept(modinfo,"LOaBIS Core"):
            tmp=0
            for y in x[5]:
                if getdat(modinfo,y):
                    modinfo=getexcept(modinfo,x)+x
                else:
                    tmp+=1
                    break
            for y in x[6]:
                if not getdat(pipmods,y):
                    tmp+=module.inst(y)
            if tmp>0:
                modinfo.pop(modinfo.index(x))
                stype[2].append(x[0])
                
        _log(str(len(stype[2]))+" modules missing dependancies",1)

    except Exception as e:
        _elog(e)
