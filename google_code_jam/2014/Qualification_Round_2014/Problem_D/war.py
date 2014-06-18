from copy import deepcopy

def melhor_ken(b, b_Ken):
    for j in b_Ken:
        if j > b:
            b_Ken.remove(j)
            return j
    j = b_Ken[0]
    b_Ken.remove(j)
    return j

with open("large.txt") as f:
    t = int(f.readline())
    for i in range(t):
        n = f.readline()
        b_Naomi = [float(j) for j in f.readline().split()]
        b_Ken = [float(j) for j in f.readline().split()]
        b_Naomi.sort()
        b_Ken.sort()
        b_Ken_deceitful = deepcopy(b_Ken)

        v_naomi_war = 0
        for j in b_Naomi:
            j_Ken = melhor_ken(j, b_Ken)
            if j > j_Ken:
                v_naomi_war += 1

        #print(v_naomi_war)

        v_naomi_d_war = 0
        for j in b_Naomi:
            if j < b_Ken_deceitful[0]:
                n_Naomi = b_Ken_deceitful[-1]-0.000001
                j_Ken = melhor_ken(n_Naomi, b_Ken_deceitful)
            else:
                n_Naomi = b_Ken_deceitful[-1]+0.000001
                j_Ken = melhor_ken(n_Naomi, b_Ken_deceitful)

            if j > j_Ken:
                v_naomi_d_war += 1

        print("Case", "#" + str(i + 1) +  ":", v_naomi_d_war, v_naomi_war)
