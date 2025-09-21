print('== CALCULADORA ==')
n1 = int(input('Digite o primeiro número: '))
op = input('Digite o operador: ')
n2 = int(input('Digite o segundo número: '))

match op:
    case '+':
        print(f'O resultado da soma é: {n1 + n2}')
    case '-':
        print(f'O resultado da subtração é {n1 - n2}')
    case '*':
        print(f'O resultado da multiplicação é {n1 * n2}')
    case '/':
        if n2 == 0:
            print('ERRO: Divisão por 0')
        else:
            print(f'O resultado da divisão é {n1 / n2}')
    case _:
        print('ERRO: Operador inválido')
