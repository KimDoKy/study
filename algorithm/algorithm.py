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
