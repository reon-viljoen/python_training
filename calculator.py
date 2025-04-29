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
    

Number_1 = int(input("Type in your first number"))
Number_2 = int(input("Type in your second number"))
Calculation = (input("Type in your calculating operation"))

answer = calculate(Number_1,Number_2,Calculation)

print(answer)