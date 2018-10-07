
def merge_sort(arr):
    arr_len = len(arr)
    if arr_len == 1:
        return arr

    mid_pos = arr_len // 2
    left_arr = arr[0:mid_pos]
    right_arr = arr[mid_pos:]
    return merge(merge_sort(left_arr), merge_sort(right_arr))


def merge(left, right):
    result = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while len(left):
        result.append(left.pop(0))
    while len(right):
        result.append(right.pop(0))

    return result

