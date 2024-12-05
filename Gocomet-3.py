f=open("Gocomet-3.1.txt",'w+')
f.writelines("hii\n hello\n heyy\n yoo")
f.close()
f=open("Gocomet-3.1.txt",'r')
print(len(f.readlines()))
f.close()
    