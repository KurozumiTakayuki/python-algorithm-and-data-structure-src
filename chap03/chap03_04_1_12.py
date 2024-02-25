from collections import deque

my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

print(my_deque[1])
x = my_deque.pop()
print(x)
del my_deque[0]
print(my_deque)
