# TO-DO: complete the helper function below to merge 2 sorted arrays
# [3, 5, 7] [1, 2, 6, 8]
def merge( arrA, arrB ):
    incrementer = 0
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[len(arrB)-1]:
            arrB.append(arrA[0])
            arrA.remove(arrA[0])
        elif arrA[0] > arrB[incrementer]:
            incrementer += 1
        else:
            arrB.insert(incrementer, arrA[0])
            arrA.remove(arrA[0])
            incrementer = 0
    return arrB

print('merging two arrays', merge([6, 7, 8, 9], [1, 2, 3, 4, 5]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        midpoint = len(arr)//2
        left = merge_sort(arr[0:midpoint])
        right = merge_sort(arr[midpoint:])
        arr = merge(left, right)
    return arr

print(merge_sort([9, 7, 6, 5, 8, 3, 2, 1, 4]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
