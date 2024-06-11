dic={}  

def CadastrarAluno():
    aluno=input('Digite o nome do Aluno: ')
    n=int(input('Quantas notas você deseja cadastrar? '))
    notasL=[]
    for i in range(n):
        notas=float(input(f'Digite a {i+1}ª nota: '))
        notasL.append(notas)
    dic.update({aluno:notasL})

def CalcMedia(notas):
    return sum(notas)/len(notas)                

def Situacao():
    if CalcMedia()>=5:
        return 'Aprovado'
    else:
        return 'Reprovado'

def MostrarNotas():
    if dic:
        for aluno, notas in dic.items():
            media = CalcMedia(notas)  
            print(f'Aluno: {aluno} \nNotas: {notas} \nMédia: {media:.2f}\n Situação: {Situacao}')
        else:
            print("Nenhum aluno cadastrado ainda.")      

while True:
    opc=int(input('Selecione a opção: \n1-Cadastrar Aluno \n2- Mostar alunos cadastrados \n3-Sair\n'))
    if opc==1:
        CadastrarAluno()
        print(50 * '-' + '\n')
    elif opc==2:
        MostrarNotas()
        print(50 * '-' + '\n')
    elif opc==3:
        print(50 * '-')
        break
    else:
         print('Opção inválida, tente novamente')