def findFirstOccurrence(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        guess = nums[mid]
        if guess == target:
            result = mid
            right = mid - 1
        elif guess < target:
            left = mid + 1
        elif guess > target:
            right = mid - 1
    return result

def findLastOccurrence(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        guess = nums[mid]
        if guess == target:
            result = mid
            left = mid + 1
        elif guess < target:
            left = mid + 1
        elif guess > target:
            right = mid - 1
    return result

nums = [2,5,5,5,6,6,8,9,9,9]

print(findLastOccurrence(nums, 5))
     

