try:
    number=int(input("Enter a number:"))
    result=10/number
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
except ValueError:
    print("Error: Invalid input. Please enter a valid number")
else:
    print(f"The result is: {result}")
print("Program by Diya Bhutani - 0221BCA041")