
try:
    f=open('cse2b.txt','ab')
except:
    print('file not found')
    
f.write(b' india is my country')

f.close()