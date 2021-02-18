# Enter your code here. Read input from STDIN. Print output to STDOUT
inputV = int(input())
a={}
for i in range(inputV):
    tmpD = str(input())
    tmpD = tmpD.split(' ')
    a[tmpD[0]]=tmpD[1]
while 1:
    try:
        s = input()
        if s in a:
            print(s+"="+a[s])
        else:
            print("Not found")
    except:
        break
