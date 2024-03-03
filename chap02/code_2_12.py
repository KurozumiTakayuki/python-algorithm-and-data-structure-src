def my_func():
    numbers = []
    for i in range(100):
        if i % 3 == 0:
            numbers.append(i)

    return numbers


def main():
    numbers = my_func()
    my_sum = 0
    for num in numbers:
        my_sum += num

    print(my_sum)


main()
