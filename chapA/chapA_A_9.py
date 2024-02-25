import timeit


def my_calc(n, m):
    """" 計測対象関数 """
    for i in range(n):
        x = i ** m


elapsed_time = timeit.timeit('my_calc(10000, 3)', globals=globals(), number=1000)
print(elapsed_time)
