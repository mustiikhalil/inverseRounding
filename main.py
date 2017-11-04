
def invRounding(number):
    if isinstance(number, float):
        return round(number) - 1 if round(number)>number else round(number) + 1


print(invRounding(1.2))
print(invRounding(1.6))
print(invRounding(1))
print(invRounding("string"))