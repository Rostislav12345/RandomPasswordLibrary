import random
def RandPass(n):
    '''
    n is for legth for pass
    
    example:
    
    RandPass(8) 
    
    output: h8l?Pd0&
    
    RandPass(18)
    
    output: PXv28u?YnxE5R@N0gG
    '''
    lower_case ="abcdefghijkmnopqrstuvwxyz"
    upper_case ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers ="01234567890"
    symbols ="=/\@#$%&!?*"
    use_for = lower_case + upper_case + numbers + symbols
    legth_for_pass = n
    password ="".join(random.sample(use_for, legth_for_pass))
    print(password)
    
    
