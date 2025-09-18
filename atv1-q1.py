n1 = int(input("Insira sua nota 1° do primeiro bimestre:"))
n2 = int(input("Insira sua nota 2° do primeiro bimestre:"))
n3 = int(input("Insira sua nota 1° do segundo bimestre:"))
n4 = int(input("Insira sua nota 2° do segundo bimestre:"))

m = (n1 + n2 + n3 + n4) / 4


if m >= 70:
    print("Aprovado")
    print("Media final:", m)

if 20 <= m < 70:
    print("O aluno está em recuperação.")  
    if m < 40:
            print("Mas é impossivel passar")
    if m >= 40:
                rec = 140 - m
                print("O aluno precisa tirar:", rec, "para recuperar sua nota")

if m < 20:
    print("Reprovado")
    print("Media final:", m)