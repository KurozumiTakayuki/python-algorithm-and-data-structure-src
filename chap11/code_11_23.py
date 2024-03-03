def fib_bu(n):
    # ボトムアップ方式
    # fib(n - 1) と fib(n - 2) を先に計算しておいた上でfib(n) を計算
    memo = [0, 1]
    i = 2
    while i <= n:
        print("n =", i, "の計算を実行しました")
        memo.append(memo[i - 1] + memo[i - 2])
        i += 1

    return memo[n]


print(fib_bu(4))
