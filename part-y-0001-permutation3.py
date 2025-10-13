import math

def permutaion_calculator(n: int, r: int) -> int:
    
    if (r > n or r < 0 or n < 0):
        
        return 0
    
    numerator = math.factorial(n)
    
    denominator = math.factorial(n - r)
    
    return numerator // denominator
        
        
print(permutaion_calculator(20, 3)) # 6840

print(permutaion_calculator(-20, 3)) # 0
