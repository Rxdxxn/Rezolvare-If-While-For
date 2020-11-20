n=eval(input("dati numarul:"))
s1=0
s2=0
a=0
b=0
c=0
d=0
for i in range (1,n+1):
    s1+=i**3  
i=0    
for i in range (1,n+1):
    a+=i
    s2=a**2  
i=0
if s1>s2:
    print("a:prima suma > a doua suma")
if s1==s2:
    print("a:sumele sunt egale")
if s2>s1:
    print("a: a doua suma > prima suma")
s1=0
s2=0
for i in range (1,n+1):
    b+=i**2
    s1=n*b  
i=0    
for i in range (1,n+1):
    c+=i
    d+=n**(i)
    s2=c+d-n
if s1>s2:
    print("b:prima suma > a doua suma")
if s1==s2:
    print("b:sumele sunt egale")
if s2>s1:
    print("b:a doua suma > prima suma")