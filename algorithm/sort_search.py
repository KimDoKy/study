# 순차 탐색
def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i
    return -1

# v_list = [23,54,75,34,76,87]
# print(search_list(v_list, 76))
# print(search_list(v_list, 99))

# 선택 정렬
def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]

d = [2, 5, 6, 4, 7]
sel_sort(d)
print(d)
