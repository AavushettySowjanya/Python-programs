'''
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
num=10
if num<=0:
    print("Enter a positive number. ")
else:
    print("Fibonacci series:",end=" ")
    for i in range(num):
        print(fibonacci(i),end=" ")

num=10
a,b=0,1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b

n=int(input("Enter the number: "))
fact=1
while n>0:
    fact=fact*n
    n=n-1

print(fact)


num="45"
print(int(num)+10)
'''

a=int(input("Enter a number: "))
print(a*a)
print(a*a*a)

