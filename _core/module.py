import sys, subprocess
from . import *
globals()["startfunc"]=[]
globals()["perfunc"]=[]
globals()["endfunc"]=[]
globals()["funcs"]=[]
globals()["cwords"]=[]
globals()["desc"]=[]

def module(name="",version="",longname="",url="",author=""):
    '''defines the module, allowing it to be loaded into loabis'''
    return True

def needs(modules=[]):
    return True

def depends(modules=[]):
    return True

def fetch(text="",start="",end="/n",default=""):
    _tmp=default
    try:
        tmp=text.split(start)[1].split(end)[0].replace("'","").replace('"',"").split(",")
    except:
        tmp=default
    for x in range(min(len(default),len(tmp))):
        _tmp[x]=tmp[x]
    return _tmp

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

def inst(mod=""):
    modi="sudo "
    if sys.platform=="win32":
        modi=""
    _log(str(mod)+" not found, installing",1)
    try:
        try:
            subprocess.call(str(modi)+"pip3 install "+str(mod),shell=True)
        except:
            subprocess.call(str(modi)+"pip install "+str(mod),shell=True)
    except Exception as e:
        _elog(e)
    if getdat(getpip(),mod):
        _log("Successfully installed",1)
        return 0
    else:
        _log("Unsuccessfull installation",1)
        return 1
