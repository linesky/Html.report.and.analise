def tabb(n:int)->str:
    s=""
    for nn in range(n):
        s=s+"    "
    return s
a:int=0
styles=True
scripts=True
triggers=False
filename="my.html"
tabsx=0
print("\x1bc\x1b[41;30m")
f1=open(filename,"r")
files=f1.read()
f1.close()
splits=files.split(">")
counter=0
counter2=0
tabsx=0
for n in splits:
    n=n.replace("\n","")
    n=n.replace("\r","")
    tags=n.split("<")
    triggers=False
    counter=0
    if len(tags)==2 and len(tags[0])>0:
        triggers=True
    counter2=0
    for ta in tags:
        
        ta=ta.strip()
        #print(ta)
        if counter==0 and len(tags)==1:
            if counter==0 and len(ta)>0:
                   
               if ta[0]!="/":
                    tabsx=tabsx+1
            if counter==0 and len(ta)>0:
                   
               if ta[0]=="/":
                    tabsx=tabsx-1

            if len(ta)>0:
               if ta=="style" or ta=="STYLE":
                   styles=False
               if ta=="script" or ta=="SCRIPT":
                   scripts=False
               if styles and scripts:
                    if triggers:
                       
                        print("\t",end="")
                   
                    print(tabb(tabsx)+"<"+tags+">")
               if ta=="/style" or ta=="/STYLE":
                   styles=True
               if ta=="/script" or ta=="/SCRIPT":
                   scripts=True
            
        else:
            
            if counter==1 and len(ta)>0:
                   
               if ta[0]!="/":
                    tabsx=tabsx+1
            if counter==1 and len(ta)>0:
                   
               if ta[0]=="/":
                    tabsx=tabsx-1

            if len(ta)>0 and counter==1:
               if ta=="style" or ta=="STYLE":
                   styles=False
               if ta=="script" or ta=="SCRIPT":
                   scripts=False
               if styles and scripts:
                   if triggers:
                       
                       print("\t",end="")
                   
                   print(tabb(tabsx)+tags[0]+"\n"+tabb(tabsx)+"<"+tags[1]+">")
               if ta=="/style" or ta=="/STYLE":
                   styles=True
               if ta=="/script" or ta=="/SCRIPT":
                   scripts=True

            
                        

               
        counter+=1
        
        
    