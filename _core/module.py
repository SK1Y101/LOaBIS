def module(name="",version="",url="",author=""):
    '''defines the module, allowing it to be loaded into loabis'''
    return True

def needs(modules=[]):
    return True

def fetch(text="",start="",end="/n",default=""):
    try:
        tmp=text.split(start)[1].split(end)[0]
    except:
        tmp=default
    return tmp.split(",")
