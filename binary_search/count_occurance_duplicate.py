def count_occurrence(nums,target):

    left = 0
    right = len(nums) - 1
    count = 0
    
    while left <= right:
        mid = (left + right) // 2
        guess = nums[mid]
        if guess == target:
            count += 1
        elif guess > target:
            right = mid - 1
        else:
            left = mid + 1
    return count


nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]


print(count_occurrence(nums, 5)) 
