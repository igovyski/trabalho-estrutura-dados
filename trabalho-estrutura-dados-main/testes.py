import Funcoes

fila = ['+', 5, 10, 15, 20, 'Fim', '-', 100, 50, 'Fim']

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
    print(fila)