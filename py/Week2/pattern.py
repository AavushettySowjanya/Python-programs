#right triange
row=5
for i in range(1,row+1):
    print("*"*i)

#square of stars
num=int(input('enter a number: '))
for i in range(num):
    for j in range(num):
         print("*",end=" ")
    print()

#inverted right tringle

rows=6
for i in range(rows,0,-1):
    print("*"*i)