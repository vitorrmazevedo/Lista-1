S = 0
lista = list(range(10))
for x in (range(10)):
    nota = float(input("Digite a nota do aluno: "))
    lista[x] = nota
media = sum(lista)/10
print("A media das notas é: ",media)
