with open('teste.txt') as f:
  T = int(f.readline())
  A = []
  M = []
  for i in range(2*T):
    A.append(int(f.readline()))
    M.append([int(i) for i in f.readline().split()])
    M.append([int(i) for i in f.readline().split()])
    M.append([int(i) for i in f.readline().split()])
    M.append([int(i) for i in f.readline().split()])

for i in range(0, 2*T, 2):
  L1 = M[i*4 + int(A[i]) - 1]
  L2 = M[(i + 1)*4 + int(A[i + 1]) - 1]
  count = 0
  for j in L1:
    if j in L2:
      count += 1
      n = j
  print("Case #{t}:".format(t = i//2 + 1), end=' ')
  if count == 1:
    print(n)
  elif count > 1:
    print('Bad magician!')
  elif count == 0:
    print('Volunteer cheated!')
