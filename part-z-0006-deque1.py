# deque -> FIFO & LIFO

from collections import deque

numbers_deque = deque()

numbers_deque.append(5)
numbers_deque.append(15)
numbers_deque.append(25)

print(numbers_deque) # deque([5, 15, 25])

numbers_deque.appendleft(35)
numbers_deque.appendleft(45)

print(numbers_deque) # deque([45, 35, 5, 15, 25])

numbers_deque.pop()

print(numbers_deque) # deque([45, 35, 5, 15])

numbers_deque.popleft()

print(numbers_deque) # deque([35, 5, 15])
