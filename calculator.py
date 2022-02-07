def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def substract(a,b):
    return a-b

def divide(a,b):
    if b==0:
        raise ValueError("Can't divide by zero")
    return a/b

if __name__ == "main":
    pass