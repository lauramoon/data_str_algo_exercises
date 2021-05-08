def bubble_sort(arr):
    """
    includes optimization if sort completes early
    descent if data almost sorted; really bad if in reverse order
    """
    for i in range(len(arr)):
        swap = False
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                swap = True
            # print(arr)
        if not swap:
            break
    return arr

def selection_sort(arr):
    """
    selects lowest item in unsorted portion, moves to next position
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
        print(arr)
    return arr

def insertion_sort(arr):
    """
    puts the selected element in correct place relative to already-sorted portion
    """
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i - 1, -1, -1):
            if temp < arr[j]:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = temp
                break
            if j == 0:
                arr[0] = temp
    return arr
            
def merge(arr1, arr2):
    idx_1 = 0
    idx_2 = 0
    arr = []
    while idx_1 < len(arr1) and idx_2 < len(arr2):
        if arr1[idx_1] < arr2[idx_2]:
            arr.append(arr1[idx_1])
            idx_1 += 1
        else:
            arr.append(arr2[idx_2])
            idx_2 += 1
    if idx_1 < len(arr1):
        arr = arr + arr1[idx_1:len(arr1)]
    else:
        arr = arr + arr2[idx_2:len(arr2)]
    return arr
                
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        length = len(arr)
        arr1 = merge_sort(arr[:length//2])
        arr2 = merge_sort(arr[length//2:])
        return merge(arr1, arr2)
