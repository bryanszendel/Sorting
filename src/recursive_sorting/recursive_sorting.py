# TO-DO: complete the helper function below to merge 2 sorted arrays
# [3, 5, 7] [1, 2, 6, 8]
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    if len(arrA) <= len(arrB):
        shorter = arrA
        longer = arrB
    else:
        shorter = arrB
        longer = arrA

    incrementer = 0
    while len(shorter) > 0:
        if shorter[0] > longer[incrementer]:
            incrementer += 1
        else:
            temp = shorter[0]
            longer.insert(incrementer, temp)
            shorter.remove(shorter[0])
            incrementer = 0
    return longer

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
