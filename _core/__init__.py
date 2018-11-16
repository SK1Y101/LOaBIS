import os, sys

ostype=sys.platform
globals()["sep"]="/"
if "win" in ostype:
    globals()["sep"]="\\"

def setup():
    module.module("LOaBIS Core","0.3.0")

def chkvar(var="",defa=""):
    if var:
        return var
    return defa

def getinfo(name=""):
    global sep
    with open(str(name)+sep+"__init__.py","r") as m:
        a=m.read()
    name,ver,lname,url,author=module.fetch(a,"module.module(",")",["","","","",""])
    depends=module.fetch("module.needs(",")",[])
    return [name,ver,lname,url,author,depends]

def setlen(var="",leng=1,tp=0,fl="0"):
    while len(var) < leng:
        if tp==1:
            var=fl+str(var)
        else:
            var=str(var)+fl
    return var[0:leng]

def getdat(data=[],search="",defa=""):
    for x in data:
        if search in x:
            return x
    return defa

def getexcept(data=[],search="",defa=""):
    tmp=data
    if list(search)!=search:
        search=[search]
    for y in search:
        for x in data:
            if y in x:
                data.pop(data.index(x))
    return chkvar(tmp,defa)

if __name__ != "__main__":
    from . import module
