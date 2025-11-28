Name="Krishna"
Age=22
Height=5.6
#using f-string format
print(f"My name is {Name}, my age is {Age} Years and my height is {Height} meters.")
print(f"My father's age is {Age*2} years.")
marks=95.675
print(f"My marks are: {marks:.2f}")
h=57.985632
print(f"my height is:{h:.3f}")
#using .format method
print("We all are {}".format('humans'))
print("{2} {1} {0}".format("directions","the","Read"))
print("a:{},b:{},c:{}".format(1,"five",10.5))
print("My marks are: %.2f" %marks)
