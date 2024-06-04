def calcularMedia (notas):
    copia = list(notas)
    copia.pop(0)
    media = sum(copia) / len(copia)
    return media

def resultado (media):
    if media >= 5:
        return 'aprovado'
    else:
        return 'Reprovado'
    
print('calculadora de media')

aluno_notas = []
aluno_notas.append(input("Digite o nome do aluno: "))

n= int(input('digite a quantidade de notas'))

for i in range (n):
    nota=float(input(f'digite a {i+1}ª nota: '))
    aluno_notas.append(nota)

m=calcularMedia(aluno_notas)
r= resultado(m)
print(f'{aluno_notas[0]}, sua mádia é {m} e você foi {r}.')