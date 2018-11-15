from . import module

def getinfo(name=""):
    with open(name+"/__init__.py","r") as m:
        m=m.read()
    name,ver,url,author=setlen(module.fetch("module.module(",")",["","","",""]),4)
    depends=fetch("module.needs(",")",[""])
    return name,ver,url,author,depends

def setlen(var="",leng=1,tp=0,fl="0"):
    while len(var) < leng:
        if list(var)==var:
            if tp==1:
                var=[]+var
            else:
                var+=[]
        else:
          if tp==1:
              var=fl+str(var)
          else:
              var=str(var)+fl
    return var[0:leng]

def setup():
    module.module("LOaBIS Core","0.3.0")

if __name__ != "__main__":
    print("core")
