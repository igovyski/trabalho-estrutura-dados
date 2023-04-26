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
                    print("A expressão é inválida.")
                    break
                last_char = pilha.pop()
                if char != pares[last_char]:
                    print("A expressão é inválida.")
                    break
            elif not char.isdigit() and char not in '+-/*':
                print("A expressão é inválida.")
                break
        else:
            if pilha:
                print("A expressão é inválida.")
            else:
                print("A expressão é válida.")
                
        i = 0
