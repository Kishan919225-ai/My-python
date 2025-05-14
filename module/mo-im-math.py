import math

# abs gives positive value
x=abs(-7.25)
print(x)

# max and min returns maxinmum and minimum value
x=max(5,7,8)
print(x)

y=min(6,7,5)
print(y)

# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x=pow(4,3)
print(x)

# to use pi 
print(math.pi)

# to use square
x=math.sqrt(64)
print(x)

# to round up a float to its nearest up and down value 
x=math.ceil(1.4)
print(x)

y=1.4
print(math.floor(y))

# copysign
x=5
y=-7

print(math.copysign(x,y))