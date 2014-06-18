n = 130
def crivo1(n):
    l = [x for x in range(2, n)]
    for el in l:
        for i in l:
            if (i % el == 0 and i is not el):
                l.remove(i)
    return l

print(crivo1(n))


def crivo2(n):
    l = [x for x in range(2, n)]
    np = [] 
    p = []
    for el in l:
        if el not in np:
            for i in l[l.index(el)+1:]:
                if (i % el == 0):
                    np.append(i)
            p.append(el)
    return p

print(crivo2(n))

def crivo3(n):
    l = [x for x in range(2, n)]
    p = []
    for el in l:
        i = 2
        while(i**2 <= el):
            if (el % i == 0):
                break
            i += 1
        else:
            p.append(el)
    return p


print(crivo3(n))
