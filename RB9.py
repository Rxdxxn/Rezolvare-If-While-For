a=eval(input(" "))
for r in range(1,a):
    s=0
    for i in range(1,r):
        if (r%i==0):
            s+=i
    if s==r:
        print(r,end=" ")