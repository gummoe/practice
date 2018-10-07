
def quick_sort(arr, left_pos, right_pos):
    if left_pos < right_pos:
        split_index = partition(arr, left_pos, right_pos)
        quick_sort(arr, left_pos, split_index - 1)
        quick_sort(arr, split_index, right_pos)

    return arr


def partition(arr, left_pos, right_pos):
    pivot = arr[left_pos]

    while left_pos < right_pos:
        while arr[left_pos] < pivot:
            left_pos += 1
        while arr[right_pos] > pivot:
            right_pos -= 1

        if left_pos <= right_pos:
            swap(arr, left_pos, right_pos)
            left_pos += 1
            right_pos -= 1

    return left_pos


def swap(arr, left_pos, right_pos):
    arr[left_pos], arr[right_pos] = arr[right_pos], arr[left_pos]

