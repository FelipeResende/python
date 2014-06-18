with open("teste.txt", 'r') as f:
    T = int(f.readline())
    for k in range(T):
        r1 = int(f.readline())
        M1 = [int(i) for j in range(4) for i in f.readline().split()]
        r2 = int(f.readline())
        M2 = [int(i) for j in range(4) for i in f.readline().split()]
        R = [j for j in M1[4*(r1 - 1):4*r1] if j in M2[4*(r2 - 1):4*r2]]
        print("Case #{k}:".format(k = k + 1), end=' ')
        if not(len(R)):
            print('Volunteer cheated!')
        elif len(R) == 1:
            print(R[0])
        else:
            print('Bad magician!')
