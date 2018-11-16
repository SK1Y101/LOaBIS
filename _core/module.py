def module(name="",version="",longname="",url="",author=""):
    '''defines the module, allowing it to be loaded into loabis'''
    return True

def needs(modules=[]):
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
