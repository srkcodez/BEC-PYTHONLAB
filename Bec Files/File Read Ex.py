
f=open("cse2b.txt",'r')
text=f.read()
for i in text:
    print(i,end="")

f.close()