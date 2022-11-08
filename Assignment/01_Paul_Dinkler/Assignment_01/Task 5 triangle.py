a,b,c = map(int, input("Write 3 numbers seperated by a space!").split())
while(not (a>0 and b>0 and c>0 and a+b>c and b+c>a and b+c>a)):
    a, b, c = map(int, input("Write 3 numbers seperated by a space!").split())

if a == b == c:
    print("equilateral triangle.")
elif a == b or a == c or b == c:
    print("isosceles triangle.")
else:
    print("scalene triangle.")
