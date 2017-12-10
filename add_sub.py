

def add(number1,number2):
    num1 = str(number1)
    num2 = str(number2)
    num1 = num1[len(num1)//2:]
    num1 += num2
    return int(num1)

print(add(212334,623))


def sub(number1,number2):
    num1 = str(number1)
    num2 = str(number2)
    num1 = num1[len(num1) // 2:]
    num1 = num2 + num1
    return int(num1)

print(sub(214,6))

