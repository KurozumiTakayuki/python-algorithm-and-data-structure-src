from collections import deque

my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.appendleft(3)
my_deque.appendleft(4)

print(my_deque)
x = my_deque.pop()
y = my_deque.popleft()

print(x, y)
