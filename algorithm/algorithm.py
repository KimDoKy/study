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

# 동명이인 찾기
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

# print(find_same_name(['tom', 'sam', 'michael', 'sam', 'billy', 'billy'])) # sam, billy 

# 팩토리얼
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

# print(fact(5)) # 120

# 팩토리얼(재귀)
def fact2(n):
    if n <= 1:
        return 1
    return n * fact2(n-1)

# print(fact2(5)) # 120

# 하노이의 탑
def hanoi(n, from_p, to_p, aux_p):
    if n == 1:
        print(from_p, "->", to_p)
        return
    
    hanoi(n - 1, from_p, aux_p, to_p)
    print(from_p, "->", to_p)
    hanoi(n - 1, aux_p, to_p, from_p)

# print("n = 1")
# hanoi(1, 1 , 3, 2)
# print("n = 2")
# hanoi(2, 1, 3, 2)
# print("n = 3")
# hanoi(3, 1, 3, 2)
