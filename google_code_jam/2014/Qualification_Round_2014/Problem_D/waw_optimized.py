from collections import deque

with open("small.txt") as f:
    t = int(f.readline())
    for i in range(t):
        n = f.readline()
        b_Naomi = sorted([float(j) for j in f.readline().split()])
        b_Ken = sorted([float(j) for j in f.readline().split()])

        b_Ken_deceitful = deque(b_Ken)

        v_naomi_war = 0
        for j in b_Naomi:
            for k in b_Ken:
                if k > j:
                    j_Ken = k
                    b_Ken.remove(k)
                    break
            else:
                j_Ken = b_Ken[0]
                b_Ken.remove(j_Ken)

            if j > j_Ken:
                v_naomi_war += 1

        v_naomi_d_war = 0
        for j in b_Naomi:
            if j < b_Ken_deceitful[0]:
                j_Ken = b_Ken_deceitful[-1]
            else:
                j_Ken = b_Ken_deceitful[0]

            if j > j_Ken:
                v_naomi_d_war += 1

            b_Ken_deceitful.remove(j_Ken)

        print("Case", "#" + str(i + 1) +  ":", v_naomi_d_war, v_naomi_war)
