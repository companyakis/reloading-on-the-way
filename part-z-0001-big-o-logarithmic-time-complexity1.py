import math

def log_n_method_1(n):
    
    return math.log2(n)
    
logn1 = log_n_method_1(128)

logn2 = log_n_method_1(100) # 0 ... 100, 0 ... 50, 51 ... 100

print(logn1) # 7

print(logn2) # 6.643856189774724
