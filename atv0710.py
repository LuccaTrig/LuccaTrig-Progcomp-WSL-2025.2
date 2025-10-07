nome = input("Digite um nome:")
altura = float(input("Digite a altura em centimeteros:")) / 100
peso = int(input("Coloque seu peso arredondado em Kilogramas:"))
imc = peso / altura ** 2

registro = {'nome': nome , 'altura' : altura , 'peso' : peso , 'imc' : imc}
print (registro)

registroIMC = []

while True:
    registroIMC.append(registro)
    print("Para adicionar mais uma pessoa digite 1")
    question = int(input())
    
    if question == 1 :
        nome = input("Digite um nome:")
        altura = float(input("Digite a altura em centimeteros:")) / 100
        peso = int(input("Coloque seu peso arredondado em Kilogramas:"))
        imc = peso / altura ** 2
        registro = {'nome': nome , 'altura' : altura , 'peso' : peso , 'imc' : imc}
        print(registro)

    else: 
        break

listaPeso = sorted(registroIMC, key=lambda x: x['peso'], reverse = True)
listaIMC = sorted(registroIMC, key=lambda x: x['imc'], reverse = True)

print(f'São {len(registroIMC)} pessoas registradas')
print(listaPeso)
print(listaIMC)