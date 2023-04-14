if __name__ == '__main__':
    number1 = input("Enter your number: ")
    number2 = input("Enter another number: ")
    number3 = input("Enter the third number: ")
    maximum = number1
    if number2 > maximum:
        maximum = number2

    if number3 > maximum:
        maximum = number3
    print('maximum is: ', maximum)
