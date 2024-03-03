from time import sleep


def sample_generator():
    print("処理開始")
    yield 'おはよう'
    print("処理再開")
    yield 'こんにちは'
    print("処理再開")
    yield 'こんばんは'


gen_obj = sample_generator()
print(next(gen_obj))
sleep(1)
print(next(gen_obj))
sleep(1)
print(next(gen_obj))
