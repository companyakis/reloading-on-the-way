import sys 

def calc_memory_consumption(n: int):
    
    some_numbers = []
    
    for i in range(n):
        
        print(f"Array length: {len(some_numbers)} - memory consumption: {sys.getsizeof(some_numbers)}")
        
        some_numbers.append(i)
        
calc_memory_consumption(20)

"""
Array length: 0 - memory consumption: 56
Array length: 1 - memory consumption: 88
Array length: 2 - memory consumption: 88
Array length: 3 - memory consumption: 88
Array length: 4 - memory consumption: 88
Array length: 5 - memory consumption: 120
Array length: 6 - memory consumption: 120
Array length: 7 - memory consumption: 120
Array length: 8 - memory consumption: 120
Array length: 9 - memory consumption: 184
Array length: 10 - memory consumption: 184
Array length: 11 - memory consumption: 184
Array length: 12 - memory consumption: 184
Array length: 13 - memory consumption: 184
Array length: 14 - memory consumption: 184
Array length: 15 - memory consumption: 184
Array length: 16 - memory consumption: 184
Array length: 17 - memory consumption: 248
Array length: 18 - memory consumption: 248
Array length: 19 - memory consumption: 248
"""
