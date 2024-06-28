import json
import time
import os


def adicionarItem (compras, item, quantidade):

    compras[item] = quantidade
    

def removerItem (compras, item):

    if item in compras:
        del compras[item]
    

def visualizar (compras):

    for item, quantiade in compras.items():
        print(f'{item}: {quantiade}')

    print()
    print('Pressione enter para continuar')
    input()
    

def salvarCompras (compras, nomeArquivo):

    with open(nomeArquivo, 'w') as arquivo:
        json.dump(compras, arquivo)
    

def carregarCompras (nomeArquivo):

    with open(nomeArquivo, 'r') as arquivo:
        return json.load(arquivo)
        

def gerenciarCompras (compras, nomeArquivo=None):

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Visualizar lista')
        print('4 - Salvar e sair')
        print('5 - Sair sem salvar')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':

            item = input('Digite o nome do item: ')
            quantidade = int(input('Digite a quantidade: '))
            adicionarItem(compras, item, quantidade)

        elif escolha == '2':

            item = input('Digite o nome do item: ')
            removerItem(compras, item)

        elif escolha == '3':

            visualizar(compras)

        elif escolha == '4':

            if nomeArquivo is None:
                nomeArquivo = input('Digite o nome do arquivo para salvar para salvar: ')

            if not nomeArquivo.endswith('.json'):
                nomeArquivo += '.json'

            salvarCompras(compras, nomeArquivo)
            break

        elif escolha == '5':
            break
        else:
            print('Opção inválida')
            time.sleep(2)


def main():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1 - Criar uma nova lista de compras')
        print('2 - Carregar uma lista existente')
        print('3 - Sair')
        escolha = input('Escolha uma opcao: ')
        
        if escolha == '1':

            compras = {}
            gerenciarCompras(compras)

        elif escolha == '2':
            print('Listas disponíveis')
            arquivos = [ arquivo for arquivo in os.listdir() if arquivo.endswith('.json')]
            if not arquivos:
                print('Nenhuma lista encontrada')
                time.sleep(2.5)
                continue

            for i, arquivo in enumerate(arquivos, 1):
                print(f'{i} {arquivo}')

            escolha = int(input('Escolha uma lista para carregar ( 0 se nenhuma ): '))

            if escolha == 0:
                continue

            if (escolha < 0) or (escolha > len(arquivos)):
                print('Opção inválida')
                time.sleep(2)
                continue
            
            nomeArquivo = arquivos[escolha - 1]
            compras = carregarCompras(nomeArquivo)
            gerenciarCompras(compras, nomeArquivo)

        elif escolha == '3':
            break
        else:
            print('Opção inválida')
            time.sleep(2)


if __name__ == '__main__':
    main()