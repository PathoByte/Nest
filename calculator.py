def calculator():
    num1 = float(input("Key in the first number: "))
    operation = input("Enter +, -, *, /:")
    num2= float(input("Key in your second number: "))

    if operation == "+":
        result = num1 + num2
        print(result)

    elif operation == "-":
        result = num1 - num2
        print(result)

    elif operation == "*":
        result = num1 * num2
        print(result)

    elif operation == "/": 
        result = num1 / num2
        print(result)

        
calculator()

