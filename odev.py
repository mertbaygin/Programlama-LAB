with open("dosya.txt","r") as file_:
    content = file_.readlines()
    #print(content)
word = input("Aranacak kelimeyi girin:")
for i in range(0,len(content)):
    s=0
    tutucu =["","","","",""]
    x=content[i].split()
    if word in x:
        while(x[s]!=word):
            s=s+1
        m=len(x)   
        for j in range(0,5):
            if(x[s+j] is not None):
                tutucu[j]=x[s+j]
                print(tutucu[:j+1])
            else:
                tutucu[j]="null"
                print(tutucu[:j+1])
                break

