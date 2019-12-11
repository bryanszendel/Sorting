# TO-DO: complete the helper function below to merge 2 sorted arrays
# [3, 5, 7] [1, 2, 6, 8]
def merge( arrA, arrB ):
    incrementer = 0
    while len(arrA) > 0:
        if arrA[0] > arrB[incrementer]:
            incrementer += 1
        else:
            arrB.insert(incrementer, arrA[0])
            arrA.remove(arrA[0])
            incrementer = 0
    return arrB

print(merge([3, 5, 7], [1, 2, 6, 8]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
