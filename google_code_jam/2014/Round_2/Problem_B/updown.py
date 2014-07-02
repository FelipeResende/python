with open("small.txt") as f:
    case = 1
    n = int(f.readline())
    while case <= n:
        tam = int(f.readline())
        T1 = [int (i) for i in f.readline().split()]
        c = sorted(T1[:])
        l = 0
        r = tam - 1
        count = 0
        for i, k in enumerate(c):
            for idx, val in enumerate(T1):
                if k == val:
                    if idx - l < (tam - i)//2:
                        while idx > l:
                            T1[idx - 1], T1[idx] = T1[idx], T1[idx - 1]
                            idx -= 1
                            count += 1
                        l += 1
                    else:
                        while idx < r:
                            T1[idx], T1[idx + 1] = T1[idx + 1], T1[idx]
                            idx += 1
                            count += 1
                        r -= 1
                    break

        print("Case #{}: {}".format(case, count))
        case += 1
