def simpCon(n):
    k = 0
    while n > 0: # 1
        d = n %10
        n //= 10 # 0
        k = k * 10 + d # k = 54321
    return k
print(simpCon(12345))


def reverseRec(n, num): #0 - 4321
    if n > 0:
        digit = n % 10  # 1
        n = n // 10  # 0
        num = digit + num * 10 # 1 + 432 * 10 = 4321
        return reverseRec(n, num) # 0  4321
    return num

def reverse(n):
    num = 0
    num = reverseRec(n, num) #1234 , 0
    return num

print(reverse(1234))