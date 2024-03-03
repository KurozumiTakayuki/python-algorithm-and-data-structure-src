def my_gcd(a, b):
    while b != 0:
        gcd = b
        b = a % b
        a = gcd

    return gcd


x = my_gcd(144, 84)
print(x)
