import sys, time, ast, os, threading
from LOaBIS import log, say
from _core import *

def main():
    logpers("Initialising")
    threading.Thread(name="Shutdown",target=chkshut).start()
    time.sleep(1)
    _funcs,_start=_fetchfuncs()
    logpers("Initialisation complete")
    print(_start)
    print(_funcs)
    while not closed:
        time.sleep(1)

def _fetchfuncs():
    try:
        _modinfo=ast.literal_eval(sys.argv[1])
    except:
        _modinfo=_fetchmods()
    logpers("fetching persistence functions")
    _funcs,_start=[],[]
    for x in _modinfo:
        exec("from "+str(x[0])+" import *")
        for y in x[10]:
            _funcs.append(y)
        for y in x[11]:
            _start.append(y)
    core=getdat(_modinfo,"LOaBIS Core")
    subprocess.call("title "+str(core[0])+" v"+str(core[1])+" - Persistence module",shell=True)
    return _funcs, _start

def chkshut():
    globals()["closed"]=False
    try:
        server=startsock(False)[0]
        logpers("LOaBIS synchronisation established")
        while True:
            if "shutdown" in msg(server):
                break
        globals()["closed"]=True
        logpers("Shutting down")
    except:
        logpers("LOaBIS not available, running seperately")

def _fetchmods():
    avoid=["__pycache__",".git"]
    modules=getexcept(next(os.walk(os.getcwd()))[1],avoid)
    modules.sort()
    modinfo,_mods=[],[]
    for x in modules:
        modinfo.append(getinfo(x))
        _mods.append(getinfo(x))
    logpers("Loading modules")
    for x in _mods:
        a,tmp=[],[]
        if x[6]:
            for y in x[6]:
                if getdat(getexcept(modinfo,x[0]),y):
                    a.append(modinfo.index(getdat(modinfo,y)))
                else:
                    tmp.append(y)
        if tmp:
            logpers(str(x[0])+" missing "+str(len(tmp))+" dependancies: "+str(tmp))
            modinfo.remove(x)
        elif a:
            modinfo.insert(1+max(a),x)
    logpers("Modules loaded")
    return modinfo

def logpers(text="null"):
    log("Persistence module: "+str(text))

def eplog(err ="",sy=1):
    log("Persistence Error: "+str(type(err))+"; "+str(err))
    if sy:
        say("Software encountered an error, consider submitting log to developers","Error",1)

if __name__=="__main__":
    main()
    #except Exception as e:
        #eplog(e)
