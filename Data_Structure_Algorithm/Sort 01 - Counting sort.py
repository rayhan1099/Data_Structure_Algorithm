# a = input("Enter your numbers: ").split(' ')
# a = [int(i) for i in a]
a = [1, 3, 7, 8, 1, 1, 3]

k = max(a)
c = [0] * (k + 1)
B = [None] * len(a)

for item in a:
    c[item] = c[item] + 1  # c[item] += 1
# print(c)

for i in range(1, len(c)):
    c[i] = c[i - 1] + c[i]
# print(c)

for item in reversed(a):
    B[c[item] - 1] = item
    c[item] -= 1

print("Sorted array: ", end=' ')
for item in B:
    print(item, end=' ')
