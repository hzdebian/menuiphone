from time import sleep
def exibir_menu():
    print('''\033[1;34m         FORMAS DE PAGAMENTO
            [ 1 ] à vista dinheiro/cheque
            [ 2 ] à vista cartão
            [ 3 ] 2x no cartão
            [ 4 ] 3x ou mais no cartão\033[m''')

def pagamento():
        if opção == 1:
            total = preço - (preço * 10 / 100)

        elif opção == 2:
            total = preço - (preço * 5 / 100)

        elif opção == 3:
            total = preço
            parcela = total / 2
            print(f'Sua compra será parcelada em 2x de R${parcela:.3f}')

        elif opção == 4:
            total = preço + (preço * 20 / 100)
            totalparc = int(input('Quantas parcelas?'))
            parcela = total / totalparc
            print(f'Sua compra será parcelada em {totalparc}x de R${parcela:.2f}')
        print(f'\033[1;34mCliente {nome}')
        print(f'\033[1mSua compra de\033[m \033[1;32mR${preço:.3f}\033[m \033[1mvai custar\033[m \033[1;32mR${total:.3f}\033[m\033[1m no final.\033[m')

def opcll ():
    if opcelular == 1:
        valor = 3.000
        print(f'Você optou pela compra do produto Apple iPhone 11 (64 GB) Preto')
        print(f'Valor: {valor:.3f}')
    elif opcelular == 2:
        valor = 2.900
        print('Você optou pela compra do produto Apple iPhone 12 (128 GB) - Branco.')
        print(F'Valor: {valor:.3f}')
    elif opcelular == 3:
        valor = 2.760
        print('Você optou pela compra do produto Samsung Galaxy S23.')
        print(f'Valor: {valor:.3f}')
    elif opcelular == 4:
        valor = 2.320
        print('Você optou pela compra do produto Smartphone Motorola Edge 40 Neo.')
        print(f'Valor: {valor:.3f}')

def opcao_celular():
    print('''\033[1;34m         Opções de compra:
            [ 1 ] Apple iPhone 11 (64 GB) Preto
            [ 2 ] Apple iPhone 12 (128 GB) - Branco
            [ 3 ] Samsung Galaxy S23
            [ 4 ] Smartphone Motorola Edge 40 Neo
            \033[m''')


def lin(msg):
    #Estiliza o Cabeçalho
    print('\033[1;34m='*10, f'{msg}', '='*10)


def cliente():
    rg = int(input('\033[1;34mRG: '))
    cpf = int(input('CPF (Apenas Números): '))
    endereco = str(input('Digite seu endereço: '))
    print(' ')


#Programa principal
lin('Hzdebian.Shop')


while True:
    try:
        nome = str(input('\033[1;34mDigite seu nome: '))
        cliente()

        opcao_celular()

        opcelular = int(input(f'\033[1;33m{nome}, digite a opção desejada: '))

        opcll()
        print(' ')
        sleep(1)

        exibir_menu()

        print(' ')

        opção = int(input('\033[0;31mQual é a opção?\033[m '))
        if opcelular == 1:
            preço = 3.000
            pagamento()
            break

        elif opcelular == 2:
            preço = 2.000
            pagamento()
            break
            
        elif opcelular == 3:
            preço = 1900
            pagamento()
            break
            
        elif opcelular == 4:
            preço == 5000
            pagamento()
            break

        else:
            #total = preço
            print('Opção inválida. Tente novamente!')

    except Exception as ValueError:
        print(f'\033[4mDigite apenas valor numérico.')


    except Exception as erro:
        print('Não foi possivel concluir seu pagamento.')
        print(f'Detalhes: {erro}')


print('\033[0;32mby @Hzyzzq')
