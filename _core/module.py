def module(name="",version="",url="",author=""):
    return True
    
def getinfo(name=""):
    with open(name+"/__init__.py","r") as m:
        m=m.read()
    name,ver,url,author=setlen(fetch("module.module(",")/n",["","","",""]),4)
    return name,ver,url,author
    
def fetch(text="",start="",end"/n",default=""):
    try:
        tmp=text.split(start)[1].split(end)[0]
    except:
        tmp=default
    except:
    return tmp.split(",")