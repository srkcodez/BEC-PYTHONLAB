

word=input('enter word')
fname=input('enter filename')

f=open(fname,'r')
text=f.read()
if(word in text):
    print("word present")
else:
    print("word not present")
f.close()