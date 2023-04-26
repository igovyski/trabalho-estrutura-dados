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