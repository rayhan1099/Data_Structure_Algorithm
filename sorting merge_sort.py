def merge(arr, start, middle, end):
    n1 = start - middle + 1
    n2 = end - middle

    L = arr[start: middle + 1]
    R = arr[middle + 1: end + 1]
    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0
    for k in range(start, end + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


def merge_sort(arr, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(arr, start, q)
        merge_sort(arr, middle + 1, end)

        merge(arr, start, middle, end)


a = input("Enter elements separated by space: ").split(' ')
ar = [int(i) for i in a]

merge_sort(ar, 0, len(ar) - 1)
print("Sorted array: ", ar)
