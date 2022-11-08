num = -1337
while(num < 0):
    num = int(input("Write a non negative number!"))
octal_num,i = 0,1
while int(num) != 0:
    octal_num += (num%8)*i
    num //= 8
    i*=10
print(octal_num)
