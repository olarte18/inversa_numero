#input


n=int(input("digite un numero: "))

#proccesing
i=0
m=n

while n!=0:
    a=n//10
    b=n-a*10
    i=i*10+b
    n=a
print("Numero inicial: "+str(m)+" Numero inverso: "+str(i))
