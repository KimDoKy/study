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

# d = [2, 5, 6, 4, 7]
# sel_sort(d)
# print(d)

# 삽입 정렬
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

# d = [2, 5, 6, 4, 7]
# ins_sort(d)
# print(d)

# 병합 정렬
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

# d = [6,8,9,7,20,34,5,2,3]
# print(d)
# merge_sort(d)
# print(d)

# 모든 친구 찾기(그래프)
def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

# 친구 친밀도 계산
def print_friend_point(g, start):
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d+1))
                done.add(x)

# fr_info = {
#     'Summer': ['John', 'Justin', 'Mike'],
#     'John': ['Summer', 'Justin'],
#     'Justin': ['Summer', 'John', 'Mike', 'May'],
#     'Mike': ['Summer', 'Justin'],
#     'May': ['Justin', 'Kim'],
#     'Kim': ['May']
# }

# print_all_friends(fr_info, 'Summer')
# print_friend_point(fr_info, 'Kim')
