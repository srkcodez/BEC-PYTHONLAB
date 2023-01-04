
with open('ht.txt','r') as f:
    f.seek(10,0)
    print(f.read(10))
    f.seek(10,1)

    f.close()
