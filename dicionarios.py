nome = input("Digite um nome:")
idade = int(input("Digite uma idade:"))

registro = {'nome': nome , 'idade' : idade }
print (registro)

loop = 'loop'

registroG = []

while loop:
    registroG.append(registro)
    print("Para adicionar mais uma pessoa digite 1")
    question = int(input())
    
    if question == 1 :
        nome = input("Digite um nome:")
        idade = int(input("Digite uma idade:"))
        registro = {'nome': nome , 'idade' : idade }
        print(registro)
        print(f'São {len(registroG)} pessoas registradas')
    else: 
        break
print(registroG)