"""     Counting Sort
This program will take n integers
and sort them using counting sort algorithm.   """

n = int(input("How many numbers? "))
arr = []  # same as -> arr = list()
# taking input
for i in range(n):
    num = int(input())
    arr.append(num)

# Building count array/list with index upto maximum number and initial value 0
largest_number = max(arr)  # max() method returns the biggest number of a list
count = [0] * (largest_number + 1)

# counting frequency of each elements
for element in arr:
    count[element] = count[element] + 1  # count[i] now contains the number of elements equal to i

# Change count[i] so that count[i] now contains actual  position of this character in output array
count[0] = count[0] - 1  # adjusting the index. Because output array will start from index 0
for i in range(1, len(count)):
    count[i] = count[i] + count[i - 1]  # now count[i] contains the number of elements less than or equal to i

# Building output array
output = [0] * len(arr)  # output array equal to input array
for item in reversed(arr):
    output[count[item]] = item
    count[item] = count[item] - 1
""" If you want to follow text book algorithm more precisely
    for i in range(len(arr)-1, -1, -1):
        output[count[arr[j]]] = arr[j]
        count[arr[j]] = count[arr[j]] - 1
"""
print("Sorted output", output)
