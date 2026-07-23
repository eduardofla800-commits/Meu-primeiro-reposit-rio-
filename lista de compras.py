lista_de_compras = []

while True:
    perguntar_item = input('diga o que voce quer adicionar na lista(ou digite sair) - ')
    
    if perguntar_item == '':
        print('voce nao digitou nenhum item\n')
        
    elif perguntar_item.lower() == 'sair':
        break
    
    else:
        lista_de_compras.append(perguntar_item)
        print(f'{perguntar_item} adicionado na lista\n')
        
while True:
    print(
'''    ==OPCOES==
1- remover item
2- adicionar item
3- sair\n
'''
)
    pergunta = input('o que vc quer fazer?(digite 1, 2 ou 3) - ')
    if pergunta == '1':
        print('sua lista de compras:\n')
        
        for item in lista_de_compras:
            print(f'item: {item}')
        pergunta = input('o que vc quer remover? - ').strip().lower()
        
        if pergunta not in lista_de_compras:
            print(f'o item {pergunta} nao esta na lista\n')
        
        else:
            print('item removido\n')
            lista_de_compras.remove(pergunta)
    
    elif pergunta == '2':
        print('sua lista de compras:\n')
        
        for item in lista_de_compras:
            print(f'item: {item}\n')
        pergunta = input('o que vc quer adicionar? - ').strip().lower()
        
        if pergunta in lista_de_compras:
            print(f'o item {pergunta} esta ja esta na lista\n')
        
        else:
            print('item adicionado\n')
            lista_de_compras.append(pergunta) 
            
    elif pergunta == '3':
        print('saindo...\n')
        break
        
    else:
        print('digite uma opcao valida, EX: 1, 2 ou 3\n')
        
print('lista completa!\n')
print('lista:\n')

if  len(lista_de_compras) == 0:
    print('vazia')

else:
    
    for item in lista_de_compras:
        print(f'item: {item}')