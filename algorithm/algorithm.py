# 1부터 n까지의 합

def sum(n):
    return n * (n+1) // 2

# palindrome

def is_palindrome(word):
    for i in range(len(word)):
        if word[i] == word[(i+1) * -1)]:
            triger = True
        else:
            triger = False
            break
    return triger

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

