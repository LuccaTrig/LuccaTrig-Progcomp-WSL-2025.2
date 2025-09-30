nome = input("Digite seu nome completo: ")
cut = nome.split(' ')

name = cut[0]
lname = cut[-1]

print(f'Seu nome é {name} e seu sobrenome é {lname}')