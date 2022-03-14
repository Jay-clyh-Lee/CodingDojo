def pushFront(arr, val):
    return [val] + arr

def popFront(arr):
    popped_val = arr[0]
    arr = arr[1:]
    return popped_val

def insertAt(arr, index, val):
    arr_split_left = arr[:index]
    arr_split_right = arr[index:]
    new_arr = arr_split_left + [val] + arr_split_right
    return new_arr