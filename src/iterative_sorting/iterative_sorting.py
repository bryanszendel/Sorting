# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    incrementer = 0
    for i in range(0, len(arr) - 1):
        cur_index = i
        cur_ind_value = arr[i]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        smallest_value = min(arr[incrementer:])
        smallest_index = arr.index(smallest_value)

        # TO-DO: swap
        if cur_ind_value > smallest_value:
            arr[cur_index] = smallest_value # 0->1
            arr[smallest_index] = cur_ind_value # 2-> 4
        incrementer += 1

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    decrementer = len(arr) 
    while decrementer != 0:
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        decrementer -= 1
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr