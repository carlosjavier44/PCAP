palabra=input("Introduce una palabra: ")
palabra=palabra.lower()

a="a"
e="e"
i="i"
o="o"
u="u"

conta=0
conte=0
conti=0
conto=0
contu=0

for letra in palabra:
    if letra==a:
        conta+=1
    elif letra==e:
        conte+=1
    elif letra==i:
        conti+=1
    elif letra==o:
        conto+=1
    elif letra==u:
        contu+=1

print("a: "+str(conta))
print("e: "+str(conte))
print("i: "+str(conti))
print("o: "+str(conto))
print("u: "+str(contu))
        