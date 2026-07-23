def productOfIntegers(number1, number2):
    product = number1 * number2

    if (product <= 1000):
        return product
    else:
        return number1 + number2

result = productOfIntegers(40, 30)
print(f"The result is {result}")