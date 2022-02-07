'''return statement =functions send python values/objects back to the caller
                    these values/objects are known as the function's return value'''


def multiply(number1=input("Write a number down: "), number2=input("Write another number down: ")):
    result = int(number1) * int(number2)
    print(result)
    return result


multiply()
