
x=input("Введи число х: ")
y=input("Введи число у: ")
expected = input("Введи ожидаемый результат: ")
expected = int(expected)
x=int(x)
y = int(y)

result = y/2 ** 3 + x
print(result == expected)