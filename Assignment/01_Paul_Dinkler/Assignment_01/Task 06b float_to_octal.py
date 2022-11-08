num = float(input("Write a non negative float number: "))
whole_num = int(num)
fraction = (num -whole_num) * 8
octal_num,i = 0,1
while num != 0:
    octal_num += (num%8)*i
    num //=8
    i *= 10
solution = str(int(octal_num)) + "."

while fraction:
    digit = int(fraction)
    fraction = (fraction-digit) *8
    solution += str(digit)

print(solution)
