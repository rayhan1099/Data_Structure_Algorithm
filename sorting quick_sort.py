def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    i += 1

    return i


def quick_sort(arr, start, end):
    if start < end:
        middle = partition(arr, start, end)

        quick_sort(arr, start, middle - 1)
        quick_sort(arr, middle + 1, end)


a = input("Enter elements separated by space: ").split(' ')
a_list = [int(i) for i in a]
quick_sort(a_list, 0, len(a_list) - 1)
print("Sorted data: ", a_list)
