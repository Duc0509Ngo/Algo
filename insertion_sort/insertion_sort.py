def insertion_sort(nums):

    for i in range(1, len(nums)):
        key = nums[i]
        hole = i
        while  hole > 0 and nums[hole - 1] > key:
            nums[hole] = nums[hole - 1]
            hole = hole - 1
        nums[hole] = key

        