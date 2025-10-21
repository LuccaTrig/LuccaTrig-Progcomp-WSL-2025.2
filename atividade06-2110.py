def decompor_saque(valor):
    notas = {}

    for nota in [100, 50, 20, 10, 5]:
        quantidade = valor // nota
        notas[nota] = quantidade
        valor = valor % nota

    return notas


print("Sacar neste caixa eletrônico só é possível se o valor for multiplo de 5 e até R$1000.")
saque = int(input("Valor a sacar:"))
resultado = decompor_saque(saque)


print(f"Valor do saque de R${saque},00:")
for nota, quantidade in resultado.items():
    print(f"{quantidade} cédula(s) de R${nota},00")
