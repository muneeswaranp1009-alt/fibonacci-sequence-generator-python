print("\n-----------Fibnoaci Generator----------")

def fib_gen(n):
    if n<=0:
        print("\nNumber Should be Positive!")
    elif n ==1:
        return [0]
    
    fib_seq = [0,1]
    
    for i in range(2,n):
        
        nxt_num = fib_seq[-1] + fib_seq[-2]
        
        fib_seq.append(nxt_num)
        
    return fib_seq

user_limit = int(input("\nHow many terms you want print:"))

result = fib_gen(user_limit)

print(f"\nFirst {user_limit} Fibonacci numbers : {result}")