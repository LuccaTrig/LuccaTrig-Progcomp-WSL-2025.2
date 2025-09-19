l = float(input("Largura:"))
c = float(input("Comprimento:"))
pdm = float(input("Pé direito:"))

t = float(input("Qual é o rendimento de 1 litro de tinta em metros quadrados?"))

litros = (4 * pdm) * (l + c) / t

print(f"Para que as paredes sejam pintadas com duas demãos serão necessarios {litros} de tinta")