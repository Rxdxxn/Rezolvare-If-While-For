m=eval(input("Dati numarul m:"))
n=eval(input("Dati numarul n:"))
puterea=''
if n>m:
    for i in range (1,n+1):
        if(m**i==n):
            puterea='da'
    if puterea=='da':
        print(n,"este putere a lui ",m) 
    else:
          print(n,"nu este putere a lui ",m)
else:       
    print("Eroare")