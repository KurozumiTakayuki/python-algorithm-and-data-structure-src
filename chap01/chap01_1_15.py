def my_gcd(a, b):
    if b == 0:
        return a

    m = a % b
    return my_gcd(b, m)


x = my_gcd(144, 84)
print(x)
