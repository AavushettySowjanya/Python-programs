'''
num=int(input("Enter a number: "))
if num>0:
    print("positive")
elif num==0:
    print("zero")
else:
    print("negative")
'''

'''
n=int(input("Enter the number: "))
if n%2==0:
    print("Even")
else:
    print("odd")
'''
'''
age=18
if age>=18:
    print("Eligible to vote")
else:
    print("not eligible")
'''
'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
op=input("Enter the operator: ")
match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
'''
'''
sum=0
for i in range(1,101):
    sum=sum+i

print(sum)
'''
'''
num=123
rev=0
while(num>0):
    temp=num%10
    rev=(rev*10)+temp
    num=num//10

print(rev)
'''
'''
for i in range(11):
    print(i)
    if(i==7):
        break
'''

for i in range(1,11):
    if i==5:
        continue
    print(i)