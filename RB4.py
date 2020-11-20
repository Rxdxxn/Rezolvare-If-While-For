from fractions import Fraction
a=eval(input("Dati numarul a:"))
b=eval(input("Dati numarul b:"))
c=eval(input("Dati numarul c:"))
d=eval(input("Dati numarul d:"))
suma=Fraction(a,b)+Fraction(c,d)
produsul=Fraction(a,b)*Fraction(c,d)
print("suma ale fractiilor este", suma)
print("produsul al fractiilor este", produsul)