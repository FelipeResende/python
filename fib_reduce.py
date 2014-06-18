from functools import reduce

fib = lambda n: reduce(lambda x, y: [x[1], x[0]+x[1]], range(n), [0, 1])

n = int(input("Digite um valor de n:"))

print(fib(n)[0])
