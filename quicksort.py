def quicksort(arr, begin = 0, end = None):
    
    if end is None:
        end = len(arr)

    if begin >= end:
        return

    pivot = partition(arr, begin, end)
    quicksort(arr, begin, pivot - 1)
    quicksort(arr, pivot + 1, end)

def partition(arr, begin, end):

    pivot = begin

    for i in range(begin + 1, end):
        if arr[i] <= arr[begin]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[begin] = arr[begin], arr[pivot]

    return pivot