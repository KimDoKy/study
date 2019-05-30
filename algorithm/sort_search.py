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
