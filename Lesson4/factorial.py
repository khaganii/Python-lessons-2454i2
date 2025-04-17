def factorial(n):
    if n == 1 or n == 0:
        return 1
    return  n * factorial(n-1)

# //2 ---- 1 * 2
# //3 ---- 2 * 3 = 6
# //4 ---- 6 * 4 = 24
# //5 ---- 24 * 5 = 120

# 5 * f(4) ->  1250
    # 4 * f(3)  ===  24
        # 3 * f(2) = 2 ==== 6
            # 2 * f(1) = 1  =====  2



print(factorial(5))