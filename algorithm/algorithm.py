# 1부터 n까지의 합

def sum(n):
    return n * (n+1) // 2

# palindrome

def is_palindrome(word):
    for i in range(len(word)):
        if word[i] == word[(i+1) * -1]:
            triger = True
        else:
            triger = False
            break
    return triger

# print(is_palindrome('호박고구마')) # false
# print(is_palindrome('토마토')) # true

# binary_search

def binary_search(element, some_list):
    s_idx = 0
    e_idx = len(some_list) - 1
    
    while s_idx <= e_idx:
        mid_idx = (s_idx + e_idx) // 2
        if element == some_list[mid_idx]:
            return mid_idx
        elif element > some_list[mid_idx]:
            s_idx = mid_idx + 1
        elif element < some_list[mid_idx]:
            e_idx = mid_idx - 1
        else:
            return None

# print(binary_search(4,[2,5,6,3,4,5,6])) # 4

# 최대값의 위치

def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx
      
# print(find_max_idx([3,5,2,4,1,7,3]))  # 5 

# 최소값의 위치

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

# print(find_min_idx([4,6,7,3,4,5,2])) # 6
