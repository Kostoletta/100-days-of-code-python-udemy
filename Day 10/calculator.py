from utility import yes_or_no_check
import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    do_continue = True
    n1 = float(input("What is the first number? "))

    while do_continue:
        n2 = float(input("What is the second number? "))

        for keys in operations:
            print(keys)

        symbol = input("Chose an operation frome the line above: ")
        result = operations[symbol](n1, n2)
        print(f"{n1} {symbol} {n2} = {result}")

        str_request = f"Do you want to continue with {result} as first number? yes/no "
        str_request_fail = "Type a valid input "

        response = input(str_request)
        while yes_or_no_check(response):
            response = input(str_request_fail)

        if response == "yes":
            n1 = result
        else:
            calculator()
calculator()