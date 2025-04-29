def calculate(value_1,value_2,operation):
    if operation == '+':
        return value_1 + value_2
    elif operation == '-':
        return value_1 - value_2
    elif operation == '*':
        return value_1 * value_2
    elif operation == '/':
        if value_2 !=0:
            return value_1 / value_2
        else:
            return "Cannot divide by zero"
    return "Invalid operation."

while True:
    first_input = input("Enter the first number or type quit to exit")
    if first_input.lower() == 'quit':
        print("Logging off")
        break

    second_input = input("Enter the second number")
    calculation = input("Enter the calculation")

    try:
        Number_1 = float(first_input)
        Number_2 = float(second_input)
        answer = calculate(Number_1,Number_2,calculation)
        print(answer)

    except ValueError:
        print("Invalid number. Please try again")