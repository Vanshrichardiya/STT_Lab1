def substract(a,b):
    return a-b

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def divide(a,b):
    if(b==0):
        return "Error"
    return a/b

a=10
b=5

print("Substraction: ")
print(substract(a,b))
print()
print("Addition: ")
print(add(a,b))
print()
print("multiplication: ")
print(multiply(a,b))
print()
print("Division: ")
print(divide(a,b))
print()

