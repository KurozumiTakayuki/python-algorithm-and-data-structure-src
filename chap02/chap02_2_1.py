def is_prime(N):
    if N == 1:
        return False

    for i in range(2, N):
        if N % i == 0:
            return False
    return True


result = is_prime(257)
print(result)
