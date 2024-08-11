#Calculator
from art import logo
#Add
def add(n1, n2):
    '''Adds two numbers together.'''
    return n1 + n2

#Subtract
def subtract(n1, n2):
    '''Subtracts two numbers.'''
    return n1 - n2

#Multiply
def multiply(n1, n2):
    '''Multiplies two numbers together.'''
    return n1 * n2

#Divide
def divide(n1, n2):
    '''Divides two numbers.'''
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        question = input(f"Type 'y' to continue calculating he {answer}, type 'n' to start a new calculation, or type 'q' to quit: ")
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if question == 'y':
            num1 = answer
        elif question == 'n':
            calculator()
        elif question == 'q':
            print("Goodbye.")
            should_continue = False
        else:
            print("You did not follow instructions. Goodbye.")
            should_continue = False

calculator()

    