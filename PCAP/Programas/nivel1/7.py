abecedario = [chr(letra) for letra in range(ord('a'), ord('z') + 1)]
count=0
for letra in abecedario:
    count+=1
    if int(count)%3==0:
        print(f"{count}.- {letra}")
        