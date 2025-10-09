# queue -> FIFO

from queue import Queue

nums = Queue()

nums.put(5)
nums.put(15)
nums.put(25)
nums.put(35)

print(nums.get()) # 5

print(nums.get()) # 15

print(nums.get()) # 25

print(nums.get()) # 35
