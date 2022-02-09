# To convert the input values to int, if they are not
def convert(a):
    try:
        return float(a)
    except ValueError:
        return str(a)

def add(a,b):
    a = convert(a)
    b = convert(b)

    # If any of the variable is string, convert both values to string and return their addition
    if isinstance(a,str) or isinstance(b,str):
        return str(a) + str(b)
    return a+b

def multiply(a,b):
    a = convert(a)
    b = convert(b)

    # If both values of string type, then multiplication can't be performed
    if isinstance(a,str) and isinstance(b,str):
        raise TypeError("Can't multiply two values of type 'str'")
    return a*b

def substract(a,b):
    a = convert(a)
    b = convert(b)

    # If any of the supplied value is string, raise error
    if isinstance(a,str) or isinstance(b,str):
        raise TypeError("Can't perform substraction on string values'")
    return a-b

        