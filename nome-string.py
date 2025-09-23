nome = int(input('Quantas palavras tem no seu nome completo?'))
info = str(input('Em sequencia escreva seu nome, sobrenome e data de nascimento:'))
cut = info.split(' ')

name = cut[0]
lname = cut[nome - 1]
dob = cut[-1]

print (f"seu nome é {name} seu ultimo nome é {lname} e a data de nascimento {dob}")