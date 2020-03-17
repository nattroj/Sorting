# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    while True:
        swapped = False

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if not swapped:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    counts = [0 for _ in range(maximum+1)]

    for i in arr:
        counts[i] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in arr[::-1]:
        arr[counts[i]-1] = i
        counts[i] -= 1

    return arr


arr = [5, 4, 3, 2, 1]

print(selection_sort(arr))
