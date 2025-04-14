def reverseRec(n, num): #12 43
    if n > 0:
        digit = n % 10  # 4 3 2
        n = n // 10  # 123 12 2
        num = digit + num * 10
        return reverseRec(n, num) #123 4 // 1 432
    return num

def reverse(n):
    num = 0
    num = reverseRec(n, num) #1234 , 0
    return num

print(reverse(1234))