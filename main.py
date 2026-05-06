def add(number1, number2):
    result = number1 + number2
    return result

def subtract(number1, number2):
    result = number1 - number2
    return result

def multiply(number1, number2):
    result = number1 * number2
    return result

def divide(number1, number2):
    result = number1 / number2
    return result

while True:
    
    try:
        print("Choose your first number")
        number1 = int(input())
        print("Choose your second number")
        number2= int(input())
        print("Which operation?")
    except ValueError:
        print("Input must be an integer\n")
        continue

    operation = input().lower()

    if operation == "+":
        print("The result is ", add(number1, number2))
    elif operation == "-":
        print("The result is ", subtract(number1, number2))
    elif operation == "*":
        print("The result is ", multiply(number1, number2))
    elif operation == "/":
        if number2 == 0:
            print("Second number (divisor) can't equal zero\n")
            continue
        print("The result is ", divide(number1, number2))
    else:
        print("Enter a correct input\n")
        continue
    print("Do you wish to continue? [Y/N] ")
    
    while True:
        answer = input().lower()
        if answer == "y":
            break
        elif answer == "n":
            break
        else: 
            print("Y or N\n")
            continue
    if answer == "y":
        continue
    elif answer == "n":
        break