# Defining counting_sort used as subroutine
def counting_sort(arr, exp):
    temp = [0] * len(arr)  # crating temporary array for digit based sorting
    count = [0] * 10  # counting array with index 0 to 9

    for item in arr:
        count[(item // exp) % 10] += 1  # counting digit based frequency

    count[0] -= 1
    for i in range(1, len(count)):
        count[i] = count[i] + count[i - 1]

    for item in reversed(arr):
        temp[count[(item // exp) % 10]] = item
        count[(item // exp) % 10] = count[(item // exp) % 10] - 1

    for i in range(len(arr)):
        arr[i] = temp[i]


# Defining radix_sort function
def radix_sort(arr):
    largest_number = max(arr)
    exp = 1
    while largest_number // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Taking inputs
arr = input("Enter numbers separated by space: ").split(' ')
arr = [int(i) for i in arr]
radix_sort(arr)
print("Sorted array: ", arr)
