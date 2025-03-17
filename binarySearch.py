def binarySearch(arr, target):
    right = len(arr)-1
    left= 0
    while left <= right:
        middle = (right + left)//2
        if target > arr[middle]:
            left = middle+1
        elif target < arr[middle]:
            right = middle - 1
        else:
            return middle
    return -1