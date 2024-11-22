num1 = float(input(f"Enter the first number:"))
num2 = float(input(f"Enter the second number:"))
operation = input("Enter the operation (+, -, *, /):")

#perform the operation based on the input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."   
else:
    result = "Invalid operation!"

#Display the result
print(f"The result of {num1} {operation} {num2} = {result}")