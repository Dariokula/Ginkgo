num = int(input("Write a number! "))
sys.stdout.write("0")
for i in range(1, num2):
    if i%3 == 0:
        continue
    else:
        sys.stdout.write(", " + str(i))
print(".")
