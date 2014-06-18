from collections import deque

with open("small.txt") as f:
    t = int(f.readline())
    for i in range(t):
        n = f.readline()
        b_Naomi = sorted(float(j) for j in f.readline().split())
        b_Ken = sorted(float(j) for j in f.readline().split())

        b_Ken_deceitful = deque(b_Ken)

        v_naomi_war = 0
        for j in reversed(b_Naomi):
            if j < b_Ken[-1]:
                b_Ken.pop()
            else:
                v_naomi_war += 1

        v_naomi_d_war = 0
        for j in b_Naomi:
            if j < b_Ken_deceitful[0]:
                j_Ken = b_Ken_deceitful.pop()
            else:
                j_Ken = b_Ken_deceitful.popleft()

            if j > j_Ken:
                v_naomi_d_war += 1

        print("Case", "#" + str(i + 1) +  ":", v_naomi_d_war, v_naomi_war)
