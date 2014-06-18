test = lambda x: x >= 15

def desafio(t):
    count = 0
    for i in range(50):
        if not t(i):
            count += 1
    print(count)

desafio(test)

def desafio1(t):
    for i in range(2**16):
        if t(i):
            break
    return(i)
        #if not t(i):
            #count += 1
        #else:
            #break
    #print(count)

#print(desafio1(test))

#test = lambda x: x == 37
#print(desafio1(test))

#test = lambda x: x > 20
#print(desafio1(test))

def seq(i):
    while(1):
        i = i + 1
        yield i


def desafio2(t, it=seq(-1)):
    for i, el in enumerate(it):
        if t(el):
            return i
        

test = lambda x: x == 15
it = seq(-1)

print("Teste 2")
print(desafio2(test, it))
