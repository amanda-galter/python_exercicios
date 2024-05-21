#senha do banco
senha_correta=123456

tentativa=3
while tentativa>0:
    senha=int(input('digite sua senha: '))
    tentativa-=1
    if senha != senha_correta:
        print(f'senha incorreta! você tem {tentativa} tentativas')
        if tentativa==0:
            print('sua senha foi bloqueada,por favor dirija-se a um de nossos caixas.')
            break
    else:
        print('olá, amanda, seja bem vida!')
        break