import sys

try:
    x = int(input("x:"))
    y = int(input("y:"))
except ValueError:
    print("Error: Invalid input")
    sys.exit()

try:
    result = x/y
except ZeroDivisionError:
    print("error cant divide by 0")
    sys.exit(1)

print("{}/{} ={}".format(x,y,result))
