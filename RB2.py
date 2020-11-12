n=eval(input("introduceti un numar:"))
s=0
y=1
for n in range(1, n+1):
    y*=n
    s+=y
print("Suma este egala cu:", s)