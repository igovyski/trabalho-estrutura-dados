def expressoes():
    i = 10
    while i != 0:
        print("======= Validador de Expressões Matemáticas =======")
        expressao = input('Digite uma expressão matemática:\n')
        pilha = []
        pares = {'(': ')', '{': '}', '[': ']'}

        for char in expressao:
            if char in pares.keys():
                pilha.append(char)
            elif char in pares.values():
                if not pilha:
                    print("INVÁLIDA")
                    break
                last_char = pilha.pop()
                if char != pares[last_char]:
                    print("INVÁLIDA")
                    break
            elif not char.isdigit() and char not in '+-/*':
                print("INVÁLIDA")
                break
        else:
            if pilha:
                print("INVÁLIDA")
            else:
                print("VÁLIDA")
                
        i = 0
