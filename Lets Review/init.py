a=int(input())
i = 0
while i<a:
    s=input()
    index = 1
    t=''
    c=''
    for x in s:
        if(index%2==0):
            c+=str(x)
        else:
            t+=str(x)
        index+=1
    print(t+" "+c)
    i+=1
