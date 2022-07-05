if __name__ == '__main__':
    s = input()
    letters = []
    upper_letters = []
    nums = []
    odd = []
    even = []
    for i in s:
        if i.isalpha() and i.islower():
            letters.append(i)
        elif i.isalpha() and i.upper():
            upper_letters.append(i)
        else:
            
            nums.append(int(i))
    nums.sort()
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    even = map(str, even)
    odd = map(str, odd)
    print(''.join(sorted(letters)) + ''.join(sorted(upper_letters)) + ''.join(sorted(odd)) + ''.join(sorted(even)))
