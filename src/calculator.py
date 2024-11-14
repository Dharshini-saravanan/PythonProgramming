def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1, num2):
    result = 0
    for i in range(num2):
        result += num1
    return result 

def div(num1,num2):
    if num2 !=0:
        return num1/num2
    else:
        return "Cannot divide by 0" 