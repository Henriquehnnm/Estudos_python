import random
import string

print('== Gerador de senhas ==')

op = int(input('Digite o número de caracteres para sua senha: '))


chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(chars) for _ in range(op))
print(f'Sua senha: {password}')


