def merge(left_list, right_list, nums):

    left_length = len(left_list)
    right_length = len(right_list)
    i, j = 0, 0

    while i < left_length and j < right_length:
        if left_list[i] <= right_list[j]:
            nums.append(left_list[i])

            i += 1
        else:
            nums.append(right_list[j])

            j += 1

    while i < left_length:
        nums.append(left_list[i])
        i += 1

    while j < right_length:
        nums.append(right_list[j])
        j += 1

    return nums


def merge_sort(nums):

    n = len(nums)
    if n < 2:
        return nums

    left_list = []
    right_list = []

    for i in range(n // 2):
        left_list.append(nums[i])

    for i in range(n // 2, n):
        right_list.append(nums[i])

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    print(left_list)
    print(right_list)

    return merge(left_list, right_list, [])


nums = [2, 3, 1, 2, 4, 3]


if __name__ == "__main__":
    print(merge_sort(nums))
