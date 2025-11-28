p=int(input("Enter the principle amount"))
r=float(input("Enter the rate of interest"))
t=int(input("Enter the time"))
a=p*(1+r/100)**t
c=a-p
print("compound interest:", c)
