print('1 - Adição (+)')
print('2 - Subtração (-)')
print('3 - Multiplicação (*)')
print('4 - Divisão (/)')
# input("Digite um valor: ")s

# FIFO
fila = ["+", 500.0, 2.0, 5.0, 10.0, 20.0]

operacao = fila.pop(0)
print(operacao)
print(fila)

# Métodos para operar com a fila inteira
def get(fila):
    item = fila[0]
    fila.pop(0)

    return item

def soma(fila):
  res = 0
  for i in fila:
    res += i
  return res

def sub(fila):
  res = 0
  for i in fila:
    res -= i
  return res

def mult(fila):
  res = 1
  for i in fila:
    res *= i
    
  return res

def divisao(fila):
  res = fila[0]
  for i in fila[1:]:
    if i == 0:
        return print('O elemento "0" não é divisivel!')
         
    else: 
        res = res / i

    return res

# print(soma(fila))
print(divisao(fila))


# PILHA - LIFO
def eliminaPrimeiro(pilha):
  pilha.pop(0)

  return fila

def adicionaNaFila(valor, fila):
  fila.append(valor)
  return fila



# print(adicionaNaFila("pessoa1",fila))
# print(adicionaNaFila("pessoa2",fila))
# print(eliminaPrimeiro(fila))