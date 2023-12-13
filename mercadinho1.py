import ast
import os
dia=0
def salvarestoque(produto):
    file = open('estoque_mercado.txt', 'w')  # Nessa parte vai ser criado um arquivo que vai ter o dicionário com o estoque de produtos
    for chave, valor in produto.items(): # pega-se a cahve e após o valor que na chave está contido
        file.write(f'{chave}: {valor}\n') # escreve no arquivo que será criado estoque_mercado txt o que tem no dicionário produto
    file.close() # fecha o arquivo

def pegarestoquedoarquivo(produto, vetornome):
    fileestoque = open('estoque_mercado.txt','r') #nessa parte vai ser pego o arquivo com o estoque
    for leitura in fileestoque: #leitura de cada linha do arquivo
        chave, valor=leitura.strip().split(':', 1) #será armazenado o valor do nome do produto na chave do dicionário e os valores(código do produto, preço, quantidade e tipo de quantidade) .strip limpa espaços em branco e .split divide em duas listas
        chave,valor=chave.strip(),valor.strip().strip(' " ') #retira os espços vazios e retira também as ['valores'] aspas
        valor=ast.literal_eval(valor)
        vetornome+=[chave]
        produto[chave]=valor
        print(valor)
    fileestoque.close()

def tabela(vetornome):
    tabela = '{}\t{}\t{}'.format('Produto', 'Preço', 'Quantidade') # tabela pra quem comprar ver os preços e quantidades de produto
    print('\t-Tabela-')
    print()
    print(tabela)
    print('=' * 50)
    for nomeproduto in vetornome:
        print('{}\t{}\t{} {}'.format(nomeproduto, produto[nomeproduto][1], produto[nomeproduto][2], produto[nomeproduto][3]))
        print('-' * 50)

	
produto={} #estoque com 1 produto base para comparações futuras
vetornome=[] #armazena o nome dos produtos no estoque
caixatotal=0
clientesdodia=0
clientes=[]
escolha=int(input('Escolha uma opção: \n1 - cadastrar produto;\n2 - Mostrar uma tabela com o estoque do supermercado;\n3 - salvar em um arquivo o estoque;\n4 - fazer uma compra;\n5 - Finalizar o dia\n0 - encerrar programa;\n'))
#como o programa vai funcionar em loop infinito coom while o usuário tem que digitar quando quer parar
if escolha > 5 or escolha <0:
    print('Essa opção não existe') #tratamento de erro se o usuário digitar -1 ou 57, não existe essas opções

while escolha !=0:
    if escolha ==1:
        opcoes=int(input('Digite o número da sua escolha\n1 - cadastro manual;\n2 - carregar de um arquivo;\n'))
        if opcoes==1:
            erro1=0
            erros2=0
            continuar=1
            nome=str(input('Digite um nome do produto: '))
            vetornome.append(nome)#armazena o nome do produto
            for i in vetornome: #leitura do vetor com nomes
                if i!=nome and len(vetornome)>1: #tartamento de erro: se o vetor tiver um produto com mesmo nome vai sempre pro else
                    erro1+=1
                    if erro1==1:
                        print('Proseguindo cadastro de produto...')
                elif i==nome and len(vetornome)==1 :
                    print('Proseguindo cadastro de produto...')       
                else:
                    erros2+=1
                    if erros2==len(vetornome):
                        print('Nome já existente')
                        del vetornome[(len(vetornome)-1)]
                        continuar=0
            if continuar==1:           
                codigoproduto=str(input('Digite o código do produto:'))
                for i in vetornome:
                    if i!=nome:
                        if len(vetornome)==1:
                            print('Código válido!')
                        elif codigoproduto != produto[i][0] and len(vetornome)>1: #verificando se o código do produto é diferente, já que ser único
                            print('Código válido!')
                            break
                        else: 
                            print('O Codigo do produto digitado no produto acima já existe!') 
                            del vetornome[(len(vetornome)-1)]   #exclui o ultimo nome adicionado, pois este não atende aos requisitos
                            continuar=0
            if continuar==1:
                    
                preco=float(input('Digite o preço sugerido:'))
                quantidadeproduto=int(input('Digite a quantidade em numeros disponivel(em ml, grama ou unidades):'))
            
                while True:
                    tipodeqtd=str(input('A quantidade acima é em ml, unidades ou gramas:'))
                    if tipodeqtd=='ml' or tipodeqtd=='gramas' or tipodeqtd=='unidades':
                        produto[nome]=[codigoproduto,preco,quantidadeproduto,tipodeqtd]
                        print('Produto adicionado com suceso')
                        break
                    else:
                        print('Tipo de quantidade não aceita,digite uma aceita(ml, unidades ou gramas)!')
        elif opcoes==2:
            pegarestoquedoarquivo(produto,vetornome)
            print('Arquivo pego com sucesso')
        else:
            print('Opcao inexistente')
        
    elif escolha==2:
        tabela(vetornome)
    
    elif escolha==3:
        salvarestoque(produto)
        print('Arquivo feito com sucesso!')
    
    elif escolha==4 and len(vetornome) ==0:
        print('Não é possivel fazer compras, pois o estoque acabou por completo ou não foi cadastrado!')
    elif escolha==4 and len(vetornome) !=0:

        maiscompras = 1
        comprados={}
        valorf = 0 #valor final da compra
        erros=0
        controle=0
        vetorcompras=[]
        prosseguir=1
        # usamos um  while, pois não sabemos em tese, quantos produtos serão comprados
        while maiscompras != 0:
            prosseguir=1
            tabela(vetornome)
            compras = str(input('Digite o nome do produto que quer comprar: '))
            for chave in vetornome:
                if chave==compras:
                    print('Nome digitado corretamente')
                    vetorcompras.append(compras)
                else:
                    erros+=1
                    if erros==len(vetornome): #tratamento de erro caso o usuário digite a chave errada
                        print('Nome errado, digite o correto por favor.')
                        prosseguir=0
                        
            if prosseguir==1:
                qtd2=0
                qtd = int(input('Digite a quantidade do produto que deseja comprar: '))
                for b in vetornome:
                    controle=1
                    if b==compras:
                        if qtd>produto[b][2]:
                            qtd2=qtd
                            print(qtd2)
                            qtd=produto[b][2]            
                        comprados[compras]=qtd                 
                        novaqtd=produto[compras][2]-qtd #atualização das quantidades
                        produto[compras][2]=novaqtd #colocando a atualização no estoque
                        for chaves in comprados:
                            valorf += produto[chaves][1] * comprados[chaves]
                        del comprados[chaves]

                        if novaqtd == 0 and qtd2>0:
                            print(f'Você só consegue comprar a quantidade total que tem no estoque {qtd}.')
                            controle=0
                            maiscompras=0
                            
                        if novaqtd==0: # Se a quantidade de um produto for 0, retira-se o mesmo do estoque
                            print('Voce comprou todo o estoque do produto em questão!')
                            controle=0
                            for i in range(len(vetornome)):
                                for j in range(len(vetorcompras)):
                                    if produto[compras][2]==0 and vetorcompras[j] == vetornome[i] :
                                        del vetornome[i]
                                        del produto[compras]
                                        break
                            

                                
            if controle==1 and prosseguir==1:
                tabela(vetornome)
            maiscompras = int(input('Quer comprar mais?\nSIM(1)\nNAO(0)\n'))

            if maiscompras != 0 and maiscompras != 1: #tratamento de erro
                print('opção inválida')

        if valorf>0:
            print(f'Valor total da compra: {valorf}')
            forma_de_pagamento=int(input('Escolha a forma de pagamento:\n1 - Pagamento a vista[1]\n2 - No cartão (até 4x com juro de 3,57%)[2]\n'))

            if forma_de_pagamento==1: #pagamento a vista
                pagamento_do_cliente=float(input('Digite a sua quantia em dinheiro para realizar o pagamento: '))
                if pagamento_do_cliente==valorf:
                    print('Pagamento feito com sucesso! sem troco.')                        
                    clientesdodia+=1
                    caixatotal+=valorf
                    salvarestoque(produto)
                                    
                elif pagamento_do_cliente>valorf:
                    print(f'Pagamento feito com sucesso! seu troco são {pagamento_do_cliente-valorf}')
                    clientesdodia+=1
                    caixatotal+=valorf
                    salvarestoque(produto)
                else:
                    print(f'EStá faltando {valorf-pagamento_do_cliente} no pagamento! por esse motivo ele não pode ser confirmado!')
                    vetornome=[]
                    produto={}
                    pegarestoquedoarquivo(produto,vetornome)
                    print('Os produtos pegos voltaraam pro estoque.')
                            
            elif forma_de_pagamento==2: #cartão
                juros = float(input('digite quanto de juros vc deseja'))
                parcela=(valorf*(juros/100))+valorf #calcula o jurros adicionado ao preço de a vista
                pagamento_no_cartao=int(input(' Digite a quantidade de vezes que quer parcelar:\n1 vez(1) 2 vezes(2) 3 vezes(3) 4 vezes(4)\n'))
                if pagamento_no_cartao==1:
                    print(f'Compra feita e parcelada em 1 vez: valor da parcela: {parcela}')                        
                    caixatotal+=parcela
                    clientesdodia+=1
                    salvarestoque(produto)
                elif pagamento_no_cartao==2:
                    print(f'Compra feita e parcelada em 2 vez: valor das parcelas: 2 x {parcela/2}')
                    caixatotal+=parcela
                    clientesdodia+=1
                    salvarestoque(produto)
                elif pagamento_no_cartao==3:
                    print(f'Compra feita e parcelada em 3 vez: valor das parcelas: 3 x {parcela/3}')
                    caixatotal+=parcela
                    clientesdodia+=1
                    salvarestoque(produto)
                elif pagamento_no_cartao==4:
                    print(f'Compra feita e parcelado em 4 vez: valor das parcelas: 4 x {parcela/4}')
                    caixatotal+=parcela
                    clientesdodia+=1
                    salvarestoque(produto)
                else:
                    print('Opção digitada invalida, os produtos voltaram pro estoque')
            else:
                print('Opção inexistente, os produtos voltaram pro estoque')
    
    elif escolha==5: #cria um relatorio do dia
        arquivo = 'finalizandodia.txt'
        if os.path.exists(arquivo):
    # Abre o arquivo em modo de leitura
            with open(arquivo,'r') as arquivo:
                # Lê todas as linhas do arquivo
                linhas = arquivo.readlines()

                # Se houver pelo menos uma linha
                if linhas:
                    # Pega a última linha do arquivo
                    ultima_linha = linhas[-1]

                    # Divide a última linha em partes usando espaço como separador
                    partes = ultima_linha.split()

                    # Pega o número do dia (assumindo que seja a primeira parte)
                    numero_do_dia = partes[0]
                    dia=int(numero_do_dia)
                    
        dia+=1
        print('Relátorio sendo criado ...')
        file2=open('finalizandodia.txt','a') 
        file2.write(f'{dia} - DIA FIALIZADO:    clientes:{clientesdodia}   Valor em caixa: {caixatotal}\n')
        file2.write('')
        file2.close()
        print(f'Clientes do dia {dia} = {clientesdodia}, caixa do dia =  {caixatotal}')
        print('Arquivo feito com sucesso!')

    else:
        print('opcao invalida') #caso o usuário digite uma das 6 opção possiveis 

    escolha=int(input('Escolha uma opção: \n1 - cadastrar produto;\n2 - Mostrar uma tabela com o estoque do supermercado;\n3 - salvar em um arquivo o estoque;\n4 - fazer uma compra;\n5 - Finalizar o dia\n0 - encerrar programa(0)\n'))
    # dentro do while a variavel escolha aparece de novo, caso o usuário queira sair do programa quando o while já está rodando