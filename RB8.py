a=eval(input("dati latura a:"))
b=eval(input("dati latura b:"))
c=eval(input("dati latura c:"))
if (a>0 and b>0 and c>0):
    if ((a<b+c) and (b<a+c) and (c<a+b)):
        if ((a==b==c)):
            print ("acest  triunghi este echilateral")
        if (((a==b) and (a!=c)) or ((b==c) and (b!=a)) or ((a==c) and (a!=b))):
            print ("acest triunghi este isoscel")
        if (a!=b!=c):
            print ("acest triunghi este scalen")
    else:
        print("Acesta nu poate fi un triunghi")
else:
    print("lungimea nu poate fi negativa")  