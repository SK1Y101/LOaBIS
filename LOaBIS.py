import sys, time
from datetime import datetime

def _say(text=""):
    for x in "System: "+str(text)+"\n":
        sys.stdout.write(x)
        time.sleep(0.003)

def _log(text="",say=False):
    y=open("log.txt","a")
    y.write("["+str(datetime.now())+"] - "+text[0].upper()+text[1:]+"\n")
    y.close()
    if say:
        _say(text)

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
