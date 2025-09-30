import math

def log_n_method_2(n):
    while n > 1:
        n = math.floor(n / 2)
        print(n)
        
log_n_method_2(128)

# 64
# 32
# 16
# 8
# 4
# 2
# 1

