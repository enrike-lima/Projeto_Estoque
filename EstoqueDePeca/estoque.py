# Início das variáveis globais
lista_peca = []
codigo_peca = 0
# Fim das variáveis globais

# Início da função cadastrarPeca()


def cadastrarPeca(codigo):
    print('\n --- Você selecionou a opção Cadastrar Peça! ---')
    print('Código da Peça: {:03d}'.format(codigo))
    nome = input('Entre com o NOME da Peça: ')
    fabricante = input('Entre com o FABRICANTE da Peça: ')
    valor = int(input('Entre com o VALOR(R$) do Peça: '))

    # dicionario armazena as variáveis 'codigo', 'nome', 'fabricante', 'valor'.
    dicionario_peca = {'codigo': codigo, 'nome': nome,
                       'fabricante': fabricante, 'valor': valor}
    # Append vem de anexar ou inserir.
    lista_peca.append(dicionario_peca.copy())
    # Move o dicionario criado para dentro da lista (faz uma cópia).

# --- Fim da função ---

# Início da função consultarPeca()


def consultarPeca():
    print('\n --- Você escolheu a opção Consultar Peça! ---')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada! \n' +
                                '-1- Consultar TODAS as Peças \n' +
                                '-2- Consultar Peças por CÓDIGO \n' +
                                '-3- Consultar Peças por FABRICANTE \n' +
                                '-4- Retornar ao MENU PRINCIPAL \n' +
                                '>> ')

        if opcao_consultar == '1':
            print('\n Você escolheu a opção Consultar TODAS as Peças!')
            for peca in lista_peca:  # Peca vai varrer toda lista de peca.
                print('------------------------------------------------')
                # Varrer todos os conjuntos chave e valor do dicionario peca.
                for key, value in peca.items():
                    # printa os campos chave, valor do dicionario.
                    print('{}: {}'.format(key, value))

        elif opcao_consultar == '2':
            print('\n Você escolheu a opção Consultar Peça por CÓDIGO!')
            valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
            for peca in lista_peca:  # Peca vai varrer toda lista de peca.
                # O valor do campo codigo desse dicionário é igual o valor desejado.
                if peca['codigo'] == valor_desejado:
                    print('-----------------------------------------------')
                    # Varrer todos os conjuntos chave e valor do dicionario peca.
                    for key, value in peca.items():
                        # printa os campos chave, valor do dicionario.
                        print('{}: {}'.format(key, value))

        elif opcao_consultar == '3':
            print('\n Você escolheu a opção Consultar Peça por FABRICANTE!')
            valor_desejado = input('Entre com o Nome do FABRICANTE: ')
            for peca in lista_peca:  # Peca vai varrer toda lista de peca.
                # O valor do campo codigo desse dicionário é igual o valor desejado.
                if peca['fabricante'] == valor_desejado:
                    print('---------------------------------------------------')
                    # Varrer todos os conjuntos chave e valor do dicionario peca.
                    for key, value in peca.items():
                        # printa os campos chave, valor do dicionario.
                        print('{}: {}'.format(key, value))

        elif opcao_consultar == '4':
            return

        else:
            print('Ops!! Opção inválida. Tente novamente!')
            continue  # volta para o início do laço.
# --- Fim da função ---


# Início da função removerPeca()

def removerPeca():
    print('\n --- Você escolheu a opçao de Remover Peça! ---')
    valor_desejado = int(input('Entre com o Código da Peça que deseja Remover: \n' +
                               '>>'))
    for peca in lista_peca:
        # O valor do campo codigo desse dicionário é igual o valor desejado.
        if peca['codigo'] == valor_desejado:
            lista_peca.remove(peca)
            print('Peça Removida com Sucesso!')

# ---- Fim da função ---


# Início Main
print('* Seja Bem-Vindo ao Controle de Estoque da Bicicletaria do David Lima *')

while True:
    menu_principal = input(' \n Escolha a Opção Desejada! \n' +
                           '-1- Cadastrar Peça \n' +
                           '-2- Consultar Peça \n' +
                           '-3- Remover Peça \n' +
                           '-4- SAIR \n' +
                           '>> ')

    if menu_principal == '1':
        codigo_peca = codigo_peca + 1
        cadastrarPeca(codigo_peca)

    elif menu_principal == '2':
        consultarPeca()

    elif menu_principal == '3':
        removerPeca()

    elif menu_principal == '4':
        break  # Encerra o laço principal (encerra o programa).

    else:
        print('Ops!! Opção inválida, Tente novamente!')
        continue  # volta para o início do laço.

# Fim Main
