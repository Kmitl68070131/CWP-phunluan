num = int(input("Enter a number less than 25\n"))
if num > 25:
    print("Error")
else:
    while num <= 25:
        print(f"Inside the loop. my variablr is {num}")
        num += 1 if num < 25 else num
