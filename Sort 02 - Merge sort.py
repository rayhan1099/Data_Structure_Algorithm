# a = input("Enter your numbers: ").split(' ')
# a = [int(i) for i in a]

def merge(a, p, q, r):
    print('in merge function: ', p, ' ', q, ' ', r)
    n1 = q - p + 1
    n2 = r - q

    L = a[p : q+1]
    R = a[q+1 : r+1]

    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1


def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2  # 5 / 2 will return 2.5
        print(p, " ", q, " ", r)
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)


a = [1, 3, 7, 8, 1, 1, 3]

merge_sort(a, 0, len(a)-1)

print(a)
