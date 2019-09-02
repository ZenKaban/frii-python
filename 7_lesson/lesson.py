def logger(function):
    def inner(x, y):
        result = function(x, y)
        print('Result is', result)
        return result
    return inner

@logger
def sum(x, y):
    return x + y

@logger
def mult(x, y):
    return x * y

sum(5,6)