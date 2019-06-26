import os, sys, subprocess

sys.path.insert(1, os.getcwd())
from LOaBIS import *

ostype=sys.platform
globals()["sep"]="/"
globals()["coremem"]=[]
globals()["self"]=str(os.path.basename(sys.argv[0]))
if "win" in ostype:
    globals()["sep"]="\\"

def setup():
    module.module("_Core","0.3.0","0.3.0","LOaBIS Core","https://github.com/SK1Y101/LOaBIS","Skiy")
    #Short name (name of folder), version (version of the mod)
    #compat (compatible loabis version), long name (name of the module itself)
    #url (if one is available), author (evident)
    module.shutdown()
    module.startup([backup],[0])
    module.depends()
    module.needs()
    module.persist()
    module.replace()

def getcore():
    log("Retrieving Backup",1)
    try:
        globals()["coremem"]=getfile("_core/corememory.txt")
        log("Backup retrieved")
    except:
        globals()["coremem"]=[]
        log("Backup not found")

def backup():
    if not coremem:
        getcore()
    cc=getrange(coremem,"<backup>","</backup>",getfile(self),0)
    log("Comparing "+str(self)+" to Backup")
    if getfile(self)!=cc:
        log("Core modified, requesting pass")
        if input("Corepass required:\n> ")!="LOaBIS":
            savefile(self,cc)
            log("Core restored to backup")
        else:
            savefile("_core/corememory.txt")
            log("Core overwrite authorised")
    log("Backup check complete",1)

def chkvar(var="",defa=""):
    if var:
        return var
    return defa

def simver(cv,mv):
    if cv.split(".")[0:2]+["0"] <= mv.split(".") <= cv.split("."):
        return 2
    elif cv.split(".")[0:2]==mv.split(".")[0:2]:
        return 1
    else:
        return 0

def getpip():
    mod=str(getmods()).replace(" ","").replace("pip","").replace("setuptools","")
    mod=''.join([i for i in mod if not i.isdigit()])
    mod = list(filter(None, mod.replace(".","").split("\\r\\n")))
    return mod[2:-1]

def getmods():
    try:
        subprocess.call("python -m pip install --upgrade pip",shell=True)
    except:
        pass
    try:
        try:
            return subprocess.check_output("pip3 list",shell=True)
        except:
            return subprocess.check_output("pip list",shell=True)
    except:
        return ""

def getinfo(name=""):
    global sep
    with open(str(name)+sep+"__init__.py","r") as m:
        a=m.read()
    _name,ver,compat,lname,url,author=module.fetch(a,"module.module(",")",[str(name),"0.0","0.0","","",""])
    depends=mklst(module.fetch(a,"module.depends(",")",[],dln=0))
    needs=mklst(module.fetch(a,"module.needs(",")",[],dln=0))
    star,pstar=mklst(splitmod(module.fetch(a,"module.startup(",")",[["",""]],"],[")))
    shut=mklst(module.fetch(a,"module.shutdown(",")",[],dln=0))
    pers=mklst(module.fetch(a,"module.persist(",")",[],dln=0))
    repl=mklst(module.fetch(a,"module.replace(",")",[],"],[",dln=0))

    return [name,ver,compat,lname,url,author,depends,needs,star,shut,pers,pstar,repl]

def mklst(var=""):
    if var in ['',['']]:
        return []
    elif var != list(var):
        return [var]
    else:
        return var

def splitmod(c=[]):
    try:
        a=[[],[],[]]
        if c[0][0] != "":
            for x in range(len(c)):
                a[int(c[x][1])].append(c[x][0])
        return [a[0]+a[2],a[1]+a[2]]
    except:
        return ["",""]

def setlen(var="",leng=1,tp=0,fl="0"):
    while len(var) < leng:
        if tp==1:
            var=fl+str(var)
        else:
            var=str(var)+fl
    return var[0:leng]

def getrange(data=[],searcha="",searchb="",defa="",ic=1):
    a,b=0,[]
    for x in data:
        if searchb in x:
            a=0
        if a!=0:
            b.append(x)
        if searcha in x:
            a=1
    if ic:
        b=[searcha]+b+[searchb]
    if b:
        return b
    else:
        return defa

def getdat(data=[],search="",defa=""):
    for x in data:
        if search in x:
            return x
    return defa

def getexcept(data=[],search="",defa=""):
    tmp=data
    for y in mklst(search):
        for x in data:
            if y in x:
                data.pop(data.index(x))
    return chkvar(tmp,defa)

def getfile(dire=""):
    with open(dire,"r") as f:
        return f.readlines()

def savefile(dire="",data=[]):
    with open(dire,"w") as f:
        f.writelines(data)

if __name__ != "__main__":
    from . import module
