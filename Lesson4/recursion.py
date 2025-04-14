def calculate_sub(a, b):
    if a > b:
        a = a-b
        return calculate_sub(a, b)
    print("ended -> ", a)
    return None

print(calculate_sub(22, 5))