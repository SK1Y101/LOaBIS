import sys, time, ast, os, threading
from LOaBIS import log, say
from _core import *

def main():
    logpers("Initialising")
    threading.Thread(name="Shutdown",target=chkshut).start()
    time.sleep(1)
    _fetchfuncs()
    logpers("Initialisation complete")
    while not closed:
        time.sleep(1)

def _fetchfuncs():
    _modinfo=ast.literal_eval(sys.argv[1])
    _funcs,_start=[],[]
    for x in _modinfo:
        exec("from "+str(x[0])+" import *")
        for y in x[10]:
            _funcs.append(y)
        for y in x[11]:
            _start.append(y)
    print(_funcs,_start)
    core=getdat(_modinfo,"LOaBIS Core")
    subprocess.call("title "+str(core[0])+" v"+str(core[1])+" - "+str(core[3]),shell=True)
    for x in _funcs:
        exec(str(x)+"()")

def chkshut():
    server=startsock(False)[0]
    logpers("
    globals()["closed"]=False
    while True:
        if "shutdown" in msg(server):
            break
    globals()["closed"]=True
    logpers("Shutting down")

def logpers(text="null"):
    log("Persistence module: "+str(text))

def eplog(err ="",sy=1):
    log("Persistence Error: "+str(type(err))+"; "+str(err))
    if sy:
        say("Software encountered an error, consider submitting log to developers","Error",1)

if __name__=="__main__":
    try:
        main()
    except Exception as e:
        eplog(e)
