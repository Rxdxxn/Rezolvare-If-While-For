z=eval(input("Dati numarul de zile: "))
if ((z<28)or(z>31)):
    print("Nu sunt luni cu asa numar de zile")
elif z==28:
    print("e luna februarie, nu e an bisect")
elif z==29:
    print("e luna februarie,e an bisect")
elif z==30:
    print("aprilie,iunie,septembrie,noiembrie")
else:
    print("ianuarie,martie,mai,iulie,august,octombrie,decembrie")