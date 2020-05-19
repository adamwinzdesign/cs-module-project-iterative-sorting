# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        if smallest_index is not cur_index:
            smallest_value = arr[smallest_index]
            arr[smallest_index] = arr[cur_index]
            arr[cur_index] = smallest_value
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True
    index = 0
    num_of_swaps = 0
    last_item = len(arr) -1

    while swapped:
        if index < last_item:
            if arr[index] > arr[index + 1]:
                largerItem = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = largerItem
                num_of_swaps += 1
            index += 1
        else:
            last_item -= 1
            if num_of_swaps == 0:
                swapped = False
            else:
                index = 0
                num_of_swaps = 0
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
