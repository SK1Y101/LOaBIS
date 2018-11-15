import sys, time, os
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
        globals()["shutdown"]=False
        modules=next(os.walk(os.getcwd()))[1]
        modules.sort()
        for x in ["__pycache__"]:
            if x in modules:
                modules.pop(modules.index(x))
        _log(str(len(modules))+" Modules located: "+str(modules))

        from _core import *
        
        modinfo=[]
        for x in modules:
            modinfo.append(module.getinfo(x))
        print(modinfo)

    except Exception as e:
        _elog(e)
