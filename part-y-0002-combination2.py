import math

def calculate_combination(n: int, r: int) -> int:
    
    if (n < 0 or r < 0 or r > n):
        
        return 0
        
    return math.factorial(n) // (math.factorial(n -r) * math.factorial(r))
    
print(calculate_combination(3, 2))
