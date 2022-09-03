from math import inf

S = int(input("Total amount: "))
v = input("Enter coin values separated by space: ").split(' ')
v = [int(i) for i in v]
m = [inf] * (S + 1)
m[0] = 0

for i in range(1, S + 1):
    for j in range(len(v)):
        if v[j] <= i:
            temp = m[i - v[j]]
            if temp + 1 < m[i]:
                m[i] = temp + 1

print("Total number of coins: ", m[S])
prinpgpvp - t(m)
