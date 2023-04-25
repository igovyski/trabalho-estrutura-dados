import Operacoes
i = 10
while i != 0:
    print('===== Menu Principal =====')
    print('1 - Operações')
    print('2 - Expressão')
    print('0 - Finalizar programa')
    print('')
    
    i = int(input('Selecione a opção desejada: '))
    
    if i == 1: Operacoes.operacoes()

    if i == 2: pass

    else: print('Não existe esta opção')
