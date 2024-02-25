memo = {0: 0, 1: 1}


def fib_td(n):
    value = memo.get(n)
    if value is None:
        # メモになければ計算する
        print("n =", n, "の計算を実行しました")
        value = fib_td(n - 1) + fib_td(n - 2)
        # メモに格納する
        memo[n] = value

    return value


print(fib_td(4))
