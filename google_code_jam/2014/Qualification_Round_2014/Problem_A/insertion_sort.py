def insertion_sort():
    aux = []
    v = [19, 3, 9, 11, 5, 17, 15, 1, 13, 7]

    for i in v:
        for j in aux:
            if (i <= j):
                aux.insert(aux.index(j), i)
                break
        else:
            aux.append(i)
    print aux


insertion_sort()
