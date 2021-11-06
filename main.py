'''import random

l=[]
for i in range(30):
  l.append(random.randint(1,365))

l.sort()
print(l)

i=0
flag=0
while(i<len(l)-1):
  if(l[i]==l[i+1]):
    print("repeats",l[i],l[i+1])
    flag=1
  i=i+1
if(flag==0):
  print("There is no repetition")

import random

rolls = [ ]
for i in range(100000):
    # randint includes the endpoints
    roll = random.randint(1, 6)
    rolls.append(roll)
print(len(rolls))
count = 0
primes = [2, 3, 5]
for roll in rolls:
    if roll in primes:
        count += 1
L = input().split(' ')  # there is a single space between the quotes
for i in range(len(L) - 1):
    if len(L[i]) > len(L[i + 1]):
        L[i], L[i + 1] = L[i + 1], L[i]

count = 0
for i in range(len(L)):
    if len(L[i]) <= len(L[-1]):
        count += 1

print(count)

n = int(input())
M = [ ]
for i in range(n):
    row = [ ]
    for num in input().split(','):
        row.append(int(num))
    M.append(row)

some_var = 0
for i in range(n):
    for j in range(n):
        some_var += M[i][j]

print(some_var)
'''
L = [90, 47, 8, 18, 10, 7]
S = [L[0]]
for i in range(1, len(L)):
    flag = True
    for j in range(len(S)):
        if L[i] < S[j]:
            before_j = S[: j]
            new_j = [L[i]]
            after_j = S[j: ]
            S = before_j + new_j + after_j
            flag = False
            break
    if flag:
        S.append(L[i])
print(S)
'''
print([[0 for i in range(5)] for j in range(3)])'''