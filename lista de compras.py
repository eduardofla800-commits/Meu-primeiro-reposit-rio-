lista_de_compras = []

while True:
    print(
'''    ==OPCOES==
1- adicionar item
2- remover item
3- ver lista
4- sair\n
'''
)
    
    pergunta = input('o que vc quer fazer? - ').lower().strip()
    
    if  pergunta == '1':
    
        pergunte = input('o que vc deseja adicionar? - ').lower().strip()
        
        if pergunte.strip() == '':
            print('voce digitou nenhum item\n')
            
        elif pergunte in lista_de_compras:
            print(f'o item {pergunte} ja esta na lista\n')
    
        else:
            lista_de_compras.append(pergunte)
            print(f'{pergunte} adicionado na lista\n')
        
    
    elif pergunta == '2':
        print('sua lista de compras:\n')
        
        for item in lista_de_compras:
            print(f'item: {item}')
        pergunta = input('o que vc quer remover? - ').strip().lower()
        
        if pergunta not in lista_de_compras:
            print(f'o item {pergunta} nao esta na lista\n')
        
        else:
            print('item removido\n')
            lista_de_compras.remove(pergunta)
    
    elif pergunta == '3':
        print('sua lista de compras:\n')
        
        print('lista de compra:\n')
        
        if len(lista_de_compras) == 0:
            print('a lista esta vazia\n')
            
        else:
        
            for item in lista_de_compras:
                print(f'item: {item}\n')
            
    elif pergunta == '4':
        print('saindo...\n')
        break
        
    else:
        print('digite uma opcao valida, EX: 1, 2, 3 ou 4\n')
        
print('lista completa!\n')
print('lista:\n')

if  len(lista_de_compras) == 0:
    print('vazia')

else:
    
    for item in lista_de_compras:
        print(f'item: {item}')