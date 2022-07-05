import time

start_time = time.time()

def binary_search(list, target):
    left = 0
    right = len(list) - 1
  
    while left <= right:
        mid = (left + right) // 2
        guess = list[mid]
        if guess == target:
            return mid
        elif guess > target:
            right = mid - 1
        else:
            left = mid + 1
    
        
         
            
end_time = time.time()
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
print(binary_search(nums, 79))
print(f'{end_time - start_time}')
