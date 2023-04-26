import Operacoes
import Expressoes

i = 10

while i != 0:
    print('\n===== Menu Principal =====')
    print('1 - Operações')
    print('2 - Expressão')
    print('3 - Exibir fila')
    print('0 - Finalizar programa')
    
    try:
        i = int(input('\nSelecione a opção desejada: '))
        
        if i == 1: Operacoes.operacoes()

        if i == 2: Expressoes.expressoes()
        
        if i == 3: print(f'\nFila: {Operacoes.fila}')
        
        if i == 0: pass

        #else: print('Não existe esta opção')
        
    except: print('Digite apenas números')
    