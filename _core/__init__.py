def setlen(var="",length=1,type=0,fill="0"):
    while length(var) < length:
        if list(var)==var:
            if type==1:
                var=[]+var
            else:
                var+=[]
        else:
          if type==1
              var=fill+str(var)
          else:
              var=str(var)+fill
    return var[0:length]

def setup():
    module.module("LOaBIS Core","0.3.0")

if __name__ != "__main__":
    print("core")
