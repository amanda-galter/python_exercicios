numeros=[]
interação=1
while interação<=5:
    escolha=int(input(f'escolha o {interação}º numero inteiro: '))
    numeros.append(escolha)
    interação+=1

soma=sum(numeros)
maximo=max(numeros)
minumo=min(numeros)
media=soma / len (numeros)
print(numeros)
print(f'a soma da nota é {soma} ')
print(f'a maior nota é {maximo} ')
print(f'a a menor nota é {minumo} ')
print(f'a media da nota é {media} ')