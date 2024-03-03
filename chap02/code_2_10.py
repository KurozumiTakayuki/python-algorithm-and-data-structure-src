def myfunc(x):
    print(id(x))


X = [1, 2, 3]
print(id(X))
myfunc(X)  # 6行目と同じidが表示される
