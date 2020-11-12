n=eval(input("introduceti anul:"))
if (n % 12 )== 0:
    s = 'Dragon'
elif (n % 12 ) == 1:
    s = 'Sobolan'
elif (n % 12 )== 2:
    s = 'Bou'
elif (n % 12 )== 3:
    s = 'Tigru'
elif (n % 12 )== 4:
    s = 'Iepure'
elif (n % 12 )== 5:
    s = 'Sarpe'
elif (n % 12 )== 6:
    s = 'Cal'
elif (n % 12 )== 7:
    s = 'Oaie'
elif (n % 12 )== 8:
    s = 'Maimuta'
elif (n % 12 )== 9:
    s = 'Cocos'
elif (n % 12 )== 10:
    s = 'Caine'
else:
    s = 'Porc'

print("anul acesta are semnul de :",s)