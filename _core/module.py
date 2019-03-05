import sys, subprocess, time
from datetime import datetime
from . import *
globals()["stafunc"]=[]
globals()["pstfunc"]=[]
globals()["perfunc"]=[]
globals()["endfunc"]=[]
globals()["funcs"]=[]
globals()["cwords"]=[]
globals()["desc"]=[]

def module(name="",version="",longname="",url="",author=""):
    '''defines the module, allowing it to be loaded into loabis'''
    return True

def needs(modules=[]):
    '''list of python dependancies for the module'''
    return True

def depends(modules=[]):
    '''list of Loabis dependancies for the module'''
    return True

def startup(funcs=[],mod=[]):
    '''list of functions and whether they should be:
    loaded at startup            0
    loaded at persistent startup 1
    loaded at both               2'''
    return True

def shutdown(funcs=[]):
    '''list of functions to be executed at shutdown'''
    return True

def persist(funcs=[]):
    '''list of functions to be executed at shutdown'''
    return True

def replace(old=[],new=[]):
    '''list of old functions and their replacements'''
    return True

def fetch(text="",start="",end="/n",default="",inter="",dln=1):
    _tmp=default
    try:
        try:
            tmp=[]
            try:
                tmp0=text.split(start+"[")[1].split("]"+end)[0].replace("'","").replace('"',"").split(inter)
            except:
                tmp0=text.split(start)[1].split(end)[0].replace("'","").replace('"',"").split(inter)
            tmp2=tmp0[1].split(",")
            tmp1=tmp0[0].split(",")
            for x in range(min(len(tmp1),len(tmp2))):
                tmp.append([tmp1[x],tmp2[x]])
        except:
            try:
                tmp=text.split(start+"[")[1].split("]"+end)[0].replace("'","").replace('"',"").split(",")
            except:
                tmp=text.split(start)[1].split(end)[0].replace("'","").replace('"',"").split(",")
    except:
        tmp=default
    if not dln:
        a=max(len(tmp),len(_tmp))
        _tmp=makelen(_tmp,a)
        tmp=makelen(tmp,a)
    for x in range(min(len(default),len(tmp))):
        _tmp[x]=tmp[x]
    return _tmp

def makelen(vr=[],ln=1):
    try:
        if vr == str(vr):
            for x in range(int(ln)):
                vr+=" "
        elif vr == list(vr):
            for x in range(int(ln)):
                vr+=['']
        return vr[0:ln]
    except:
        return vr

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
