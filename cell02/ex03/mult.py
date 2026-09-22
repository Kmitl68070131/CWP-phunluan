f_num = int(input("Enter the first number:\n"))
l_num = int(input("Enter the second number:\n"))
result = f_num * l_num
print(f"{f_num} x {l_num} = {result}")

if result < 0:
    print("This number is negative.")
elif result > 0:
    print("This number is positive.")
else:
    print("This result is positive and negative.")
