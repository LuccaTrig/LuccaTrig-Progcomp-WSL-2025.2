frase = input("Digite uma frase: ").strip()


fraseMin = frase.lower()

countA = fraseMin.count('a')

firstA =fraseMin.find('a')

lastA = fraseMin.rfind('a')

print(f"A letra 'A' aparece {countA} vezes na frase. Onde aparede primeira vez na posição {firstA} e por ultimo na posição {lastA}")