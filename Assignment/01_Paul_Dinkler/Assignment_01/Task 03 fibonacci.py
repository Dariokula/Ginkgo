num = int(input("Write a number: "))
sys.stdout.write("0")
a = 1
b = 1
while(a<= num):
    sys.stdout.write(", " + str(a))
    c = a+b
    a = b
    b = c
print(".")
