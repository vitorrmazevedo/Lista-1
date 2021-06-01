sentence = "Practice Problems to Drill List Comprehension in Your Head."
lista = list(sentence)
for i in sentence:
    if i == "a":
        lista.remove(i)
    elif i == "e":
        lista.remove(i)
    elif i == "i":
        lista.remove(i)
    elif i == "o":
        lista.remove(i)
    elif i == "u":
        lista.remove(i)
print(lista)
