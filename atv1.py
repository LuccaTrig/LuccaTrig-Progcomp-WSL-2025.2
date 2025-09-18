n1 = int(input("Insira sua nota 1° do primeiro bimestre:"))
n2 = int(input("Insira sua nota 2° do primeiro bimestre:"))
n3 = int(input("Insira sua nota 1° do segundo bimestre:"))
n4 = int(input("Insira sua nota 2° do segundo bimestre:"))

m = (n1 + n2 + n3 + n4) / 4
nr = 140 - m
mf = m + nr / 2

if m >= 70:
    print("Aprovado")

if 20 <= m < 70:
    print("Em recuperação,precisa tirar")
    print(nr)
    print("Media final")
    print(mf)

if m < 20:
    print("Reprovado")