def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n-1) * factorial(n)

# //2 ---- 1 * 2
# //3 ---- 2 * 3 = 6
# //4 ---- 6 * 4 = 24
# //5 ---- 24 * 5 = 120

print(factorial(0))