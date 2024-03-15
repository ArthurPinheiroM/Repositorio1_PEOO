frase = input("Digite uma frase ")
d = frase.split()
for x in d:
    num = len(x)
    print(x[num-1],end = "")