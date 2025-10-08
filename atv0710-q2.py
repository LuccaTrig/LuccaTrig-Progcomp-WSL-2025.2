pessoas = [{"nome": "joao", "idade": 25}, {"nome": "paulo", "idade": 54},
            {"nome": "maria", "idade": 32}, {"nome": "marcos", "idade": 17},
              {"nome": "jessica", "idade": 44}, {"nome": "isis", "idade": 22}, 
              {"nome": "sofia", "idade": 18}] 

listaNomes = []
listaIdades = []

for pessoas in pessoas:
    listaNomes.append(pessoas['nome'])
    listaIdades.append(pessoas['idade'])
print(listaNomes , listaIdades)