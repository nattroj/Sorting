# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    while len(arrA) and len(arrB):
        index = len(merged_arr) - elements

        if arrA[0] < arrB[0]:
            merged_arr[index] = arrA.pop(0)
        else:
            merged_arr[index] = arrB.pop(0)

        elements -= 1

    while len(arrA):
        index = len(merged_arr) - elements
        merged_arr[index] = arrA.pop(0)
        elements -= 1

    while len(arrB):
        index = len(merged_arr) - elements
        merged_arr[index] = arrB.pop(0)
        elements -= 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr

    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    arr = merge(left, right)

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
def timsort(arr):

    return arr
