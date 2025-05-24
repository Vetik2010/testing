#canculator
a = float(input("Ведіть перше значення "))
b = float(input("Ведіть друге значення "))
operation = input("яка операція -, +, /, * : ")
result = 0
if operation == "+":
    result = a + b
    print(result)
elif operation == "-":
    result = a - b
    print(result)
elif operation == "/":
    result = a / b
    print(result)
elif operation == "*":
    result = a * b
    print(result)