import sys, time, os
from datetime import datetime

def _say(txt=""):
    for x in "System: "+str(txt)+"\n":
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
        for x in ["_core","__pycache__"]:
            if x in modules:
                modules.pop(modules.index(x))
        _log(str(len(modules))+" Modules located: "+str(modules))

    except Exception as e:
        _log("Software closed unexpectedly, consider submitting log to developers",1)
        _log("Error: "+str(type(e))+"; "+str(e)+"\n")
