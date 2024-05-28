lista_compras= []

num_produtos = int(input('quantos produtos você deseja adicionar?: '))

for i in range(num_produtos):
    produto=input('nome do produto: ')
    quantidade=int(input('quantidade: '))
    lista_compras.append([produto,quantidade])

print('lista de compras: ')
for produto, quantidade in lista_compras:
    print(f'produto: {produto} - quantidade: {quantidade}')