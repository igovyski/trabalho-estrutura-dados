fila = []

def operacoes():
        i = 10
        while i != 0:
            print('===== OPERAÇÕES =====')
            print('1 – Adicionar Operação na Fila')
            print('2 - Executar Próxima Operação da Fila')
            print('3 – Executar Todas as Operações da Fila')
            print('0 – Voltar para o menu principal')
            print('')

            try:
                i = int(input('Selecione a opção desejada: '))

                if i == 1: addOperacaoFila()

                if i == 2: pass

                if i == 3: pass
            
                else: print('Não existe esta opção')
            
            except: print('Digite apenas números.')


def addOperacaoFila():
    i = 10
    while i != 0:
        print('1 - Adição (+)')
        print('2 - Subtração (-)')
        print('3 - Multiplicação (*)')
        print('4 - Divisão (/)')
        
        try:
            i = int(input('Selecione a opção desejada: '))

            if i == 1: adicao()

            if i == 2: subtracao()
            
            if i == 3: multiplicacao()

            if i == 4: divisao()
        
        except: print('Não existe esta opção')


def adicao():
    qtdeItensOperacao = input("Quantos valores serão incluidos nessa operação?\n")
    
    fila.append('+')
    
    # Fazer um for para a quantidade de itens que serão discrimidados acima.
    for j in range(1, qtdeItensOperacao + 1):
        fila.append(int(input(f'{j} - Digite o valor: ')))



def subtracao():
    qtdeItensOperacao = input("Quantos valores serão incluidos nessa operação?\n")
    
    fila.append('-')
    
    for j in range(1, qtdeItensOperacao + 1):
        fila.append(int(input(f'{j} - Digite o valor: ')))


def multiplicacao():
    qtdeItensOperacao = input("Quantos valores serão incluidos nessa operação?\n")

    fila.append('*')
    
    for j in range(1, qtdeItensOperacao + 1):
        fila.append(int(input(f'{j} - Digite o valor: ')))


def divisao():
    qtdeItensOperacao = input("Quantos valores serão incluidos nessa operação?\n")

    fila.append('/')
    
    for j in range(1, qtdeItensOperacao + 1):
        fila.append(int(input(f'{j} - Digite o valor: ')))

