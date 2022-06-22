
f1=open('cse2b.txt','r')
f2=open("cse2b copy.txt",'w')
f2.write(f1.read())
f1.close()
f2.close()