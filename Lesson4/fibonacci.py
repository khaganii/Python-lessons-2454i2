# level = {}
# def fibonacci(n):
#     if n in level:
#         return level[n]
#     if n == 1 or n == 2:
#         return 1
#     s1 = fibonacci(n-1)
#     s2 = fibonacci(n-2)
#     level[n] = s1 + s2
#     return level[n]

def fib(n):
    f = 1
    s = 1
    current = 2
    for i in range(3, n+1):
        current = f+s
        s = f
        f = current
    return current
print(fib(100))
