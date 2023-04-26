import Funcoes

fila = []

def operacoes():
        i = 10
        while i != 0:
            print('\n===== OPERAÇÕES =====')
            print('1 - Adicionar Operação na Fila')
            print('2 - Executar Próxima Operação da Fila')
            print('3 - Executar Todas as Operações da Fila')
            print('0 - Voltar para o menu principal')

            try:
                i = int(input('\nSelecione a opção desejada: '))

                if i == 1: addOperacaoFila()

                if i == 2: proximaOperacaoFila()

                if i == 3: todasOperacoesFila()
            
            except: print('Não existe essa opção')


def addOperacaoFila():
    i = 10
    while i != 0:
        print('\n===== Operações =====')
        print('1 - Adição (+)')
        print('2 - Subtração (-)')
        print('3 - Multiplicação (*)')
        print('4 - Divisão (/)')
        print('0 - Voltar')
        
        try:
            i = int(input('\nSelecione a opção desejada: '))

            if i == 1: adicao()

            if i == 2: subtracao()
            
            if i == 3: multiplicacao()

            if i == 4: divisao()
        
        except: print('Não existe essa opção')


def adicao():
    try:
        qtdeItensOperacao = int(input("\nQuantos valores serão incluidos nessa operação?\n"))
        
        fila.append('+')
        
        # Fazer um for para a quantidade de itens que serão discrimidados acima.
        for j in range(1, qtdeItensOperacao + 1):
            fila.append(int(input(f'{j} - Digite o valor: ')))
            
        fila.append('Fim')
    
    except: print('Não existe esta opção')


def subtracao():
    try:
        qtdeItensOperacao = int(input("\nQuantos valores serão incluidos nessa operação?\n"))
        
        fila.append('-')
        
        for j in range(1, qtdeItensOperacao + 1):
            fila.append(int(input(f'{j} - Digite o valor: ')))
            
        fila.append('Fim')
            
    except: print('Não existe esta opção')


def multiplicacao():
    try:
        qtdeItensOperacao = int(input("\nQuantos valores serão incluidos nessa operação?\n"))

        fila.append('*')
        
        for j in range(1, qtdeItensOperacao + 1):
            fila.append(int(input(f'{j} - Digite o valor: ')))
            
        fila.append('Fim')

    except: print('Não existe esta opção')


def divisao():
    try:
        qtdeItensOperacao = int(input("\nQuantos valores serão incluidos nessa operação?\n"))

        fila.append('/')
        
        for j in range(1, qtdeItensOperacao + 1):
            fila.append(int(input(f'{j} - Digite o valor: ')))
        
        fila.append('Fim')

    except: print('Não existe esta opção')


def proximaOperacaoFila():
    try:
        for i in fila:
            if fila[0] == '+':
                print('\nAdição')
                
                fila.pop(0)
                valores = []
                aux = 0
                
                for i in fila:
                    if i == 'Fim':
                        aux = fila.index(i)
                        valores = fila[0:aux]
                        break
                    
                del fila[0:aux+1]
                print(f'Valores: {valores}')
                print(f'Resultado: {Funcoes.soma(valores)}')
                break
                
                
            if fila[0] == '-':
                print('\nSubtração')
                
                fila.pop(0)
                valores = []
                aux = 0
                
                for i in fila:
                    if i == 'Fim':
                        aux = fila.index(i)
                        valores = fila[0:aux]
                        break
                
                del fila[0:aux+1]
                print(f'Valores: {valores}')
                print(f'Resultado: {Funcoes.sub(valores)}')
                break
                
            
            if fila[0] == '*':
                print('\nMultiplicação')

                fila.pop(0)
                valores = []
                aux = 0
                
                for i in fila:
                    if i == 'Fim':
                        aux = fila.index(i)
                        valores = fila[0:aux]
                        break
                
                del fila[0:aux+1]
                print(f'Valores: {valores}')
                print(f'Resultado: {Funcoes.mult(valores)}')
                break
                
                
            if fila[0] == '/':
                print('\nDivisão')
                
                fila.pop(0)
                valores = []
                aux = 0
                
                for i in fila:
                    if i == 'Fim':
                        aux = fila.index(i)
                        valores = fila[0:aux]
                        break
                
                del fila[0:aux+1]
                print(f'Valores: {valores}')
                print(f'Resultado: {Funcoes.divisao(valores)}')
                break
            
            
    except: print('\nNão existem operações na fila')
    

def todasOperacoesFila():
    try:
        if fila[0] == '+':
            print('\nAdição')
            
            fila.pop(0)
            valores = []
            aux = 0
            
            for i in fila:
                if i == 'Fim':
                    aux = fila.index(i)
                    valores = fila[0:aux]
                    break
                
            del fila[0:aux+1]
            print(f'Valores: {valores}')
            print(f'Resultado: {Funcoes.soma(valores)}')
            
            
        if fila[0] == '-':
            print('\nSubtração')
            
            fila.pop(0)
            valores = []
            aux = 0
            
            for i in fila:
                if i == 'Fim':
                    aux = fila.index(i)
                    valores = fila[0:aux]
                    break
            
            del fila[0:aux+1]
            print(f'Valores: {valores}')
            print(f'Resultado: {Funcoes.sub(valores)}')
            
        
        if fila[0] == '*':
            print('\nMultiplicação')

            fila.pop(0)
            valores = []
            aux = 0
            
            for i in fila:
                if i == 'Fim':
                    aux = fila.index(i)
                    valores = fila[0:aux]
                    break
            
            del fila[0:aux+1]
            print(f'Valores: {valores}')
            print(f'Resultado: {Funcoes.mult(valores)}')
            
            
        if fila[0] == '/':
            print('\nDivisão')
            
            fila.pop(0)
            valores = []
            aux = 0
            
            for i in fila:
                if i == 'Fim':
                    aux = fila.index(i)
                    valores = fila[0:aux]
                    break
            
            del fila[0:aux+1]
            print(f'Valores: {valores}')
            print(f'Resultado: {Funcoes.divisao(valores)}')
            
            
    except: print('\nNão existem operações na fila')
