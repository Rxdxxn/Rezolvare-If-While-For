n=eval(input("Introduceti varsta lui Mihai:"))
a=1
b=1
for i in range(1,n+1):
    a=a*2+i
print("la varsta de",n,"ani, Mihai a primit",a,"dolari")

c=0
while (b<100):
    c=c+1
    b=b*2+c
print("Mihai a primitmai mult de 100$ la varsta de",c,"ani")
