
f=open('cse2b.txt','r')
text=f.read()
cc=0
wc=0
lc=1
for i in text:
    if(i.isalnum()):
        cc+=1
    if(i==' '):
        wc+=1
    if(i=='\n'):
        lc+=1
print("number of characters:%d\n,number words:%d\n number of lines:%d\n "%(cc,wc,lc))

f.close()