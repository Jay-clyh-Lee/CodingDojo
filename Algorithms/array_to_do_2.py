
def reverse(arr):
    k = len(arr)
    for i in range(k//2):
        temp = arr[i]
        arr[i] = arr[k-1-i]
        arr[k-1-i] = temp
    return arr

def rotate(arr, steps):
    k = len(arr)
    if steps < 0:
        steps = abs(steps)
        arr = arr[steps:k] + arr[:steps]
    else:
        arr = arr[k-steps:] + arr[:k]
    return arr

def filterRange(arr, min_val, max_val):
    k = len(arr)
    nextIndex = 0
    for i in range(k):
        if (arr[i] >= min_val or arr[i] <= max_val):
            arr[nextIndex] = arr[i]
            nextIndex += 1
    
    return arr[:nextIndex]

def concat(arr1, arr2):
    k = len(arr1)
    concat_arr = []
    for i in range(k):
        concat_arr[i] = arr1[i]
    for j in range(len(arr2)):
        concat_arr[j+k-1] = arr2[j]
    return concat_arr