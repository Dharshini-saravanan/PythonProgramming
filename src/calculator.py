def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def div(num1,num2):
    if num2 !=0:
        return num1/num2
    else:
        return "Cannot divide by 0"
num1 = 10
num2 = 5
print("Addition: ",add(num1,num2))
print("Subtraction: ",sub(num1,num2))
print("Multiplication: ",multiply(num1,num2))
print("Division: ",div(num1,num2))