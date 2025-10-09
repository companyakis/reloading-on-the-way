# stack -> LIFO

# python lists ~ LifoQueue

from queue import LifoQueue

# list
nums1 = []
nums1.append(5)
nums1.append(15)
nums1.append(25)
nums1.append(35)

print(nums1) # [5, 15, 25, 35]

nums1.pop()
print(nums1) # [5, 15, 25]
nums1.pop() 
print(nums1) # [5, 15]

# LifoQueue
nums2 = LifoQueue()
nums2.put(5)
nums2.put(15)
nums2.put(25)
nums2.put(35)

print(nums2.get()) # 35
print(nums2.get()) # 25
print(nums2.get()) # 15
print(nums2.get()) # 5

# print(nums2.get()) 
