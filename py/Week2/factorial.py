def factorial(n):
    #if n==0 or 1 then fact will be 1
    if n<=1:
        return 1
    #recursion for each integer
    else:
        return n*factorial(n-1)
    
num=4
print(factorial(num))
