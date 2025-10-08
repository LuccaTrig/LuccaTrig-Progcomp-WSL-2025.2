
nome = input("Escreva seu nome: ")
teste1 = float(input("Digite o resultado do teste 1: "))
teste2 = float(input("Digite o resultado do teste 2: "))
media = (teste1 + teste2) / 2
registro = {'nome': nome , 'teste1' : teste1 , 'teste2' : teste2 , 'media' : media}

registroMedia = []

while True:
    registroMedia.append(registro)
    print("Para adicionar mais uma pessoa digite 1")
    question = int(input())
    
    if question == 1 :
        nome = input("Escreva seu nome:")
        print(registro)
        teste1 = float(input("Digite o resultado do teste 1: "))
        teste2 = float(input("Digite o resultado do teste 2: "))
        media = (teste1 + teste2) / 2
        registro = {'nome': nome , 'teste1' : teste1 , 'teste2' : teste2 , 'media' : media}

    else: 
        break

aprovados = []
reprovados = []

for aluno in registroMedia:
    aprovados.append(aluno) if aluno['media'] >= 5 else reprovados.append(aluno)

print(f'foram aprovados os alunos: {aprovados} e reprovados: {reprovados}')