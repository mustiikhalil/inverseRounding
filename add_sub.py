

def add(number1,number2):
    x = str(number1)
    y = str(number2)
    num1 = []
    for i in x:
        num1.append(i)

    num1 = num1[len(num1)//2:]

    for i in y:
        num1.append(i)
    stringNum = ''
    for i in num1:
        stringNum += i

    return int(stringNum)


print(add(214,6))


def sub(number1,number2):
    x = str(number1)
    y = str(number2)
    num1 = []
    num2 = []
    for i in x:
        num1.append(i)

    num1 = num1[len(num1)//2:]

    for i in y:
        num2.append(i)
    num1 = num2 + num1

    stringNum = ''
    for i in num1:
        stringNum += i

    return int(stringNum)

print(sub(214,6))
