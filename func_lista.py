def list_from_str(str):
    lista = []
    l = []
    for i in str.split():
        if i.isalpha():
            if l:
                lista.append(l)
                l = []
        l.append(i)
    if l:
        lista.append(l)
    return lista

lista = list_from_str("Felipe 12 1 54 Danilo 1 7 12 Ricardo 3 6 9 9")
print(lista)
