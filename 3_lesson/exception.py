from random import random

def crazy_exception():
    ran = random()
    if ran <= 0.33:
        raise ValueError('This is value error')
    elif ran > 0.33 and ran <= 0.66:
        raise TypeError('This is type error')
    elif ran > 0.66:
        raise RuntimeError('This is RuntimeError error')

for i in range(10):
    try:
        crazy_exception()
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except RuntimeError as e:
        print(e)