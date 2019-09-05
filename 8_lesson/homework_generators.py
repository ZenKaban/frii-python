def random_generator():
    import random
    num = 0
    while True:
        value = random.random()
        yield value
        num += 1
        
        
def range_generator(start=0, end=1, step=1):
    current_status = start
    while current_status < end:
        yield current_status
        current_status = current_status + step


def map_generator(function, lst):
    pos = 0
    while pos < len(lst):
        yield function(lst[pos])
        pos += 1
        

def enum_generator(lst, start):
    enum = range_generator(start=start, end=len(lst)+start)
    for item in lst:
        try:
            yield next(enum), item
        except StopIteration:
            break


def zip_generator(lst1, lst2):
    pos = 0
    while pos < min(len(lst1), len(lst2)):
        yield (lst1[pos], lst2[pos])
        pos += 1


## testing enum_generator
# lst = ['one', 'two', 'three']
# lst2 = ['big', 'small', 'huge']
#
# print(dict(zip_generator(lst, lst2)))

## testing enum_generator
# lst = ['one', 'two', 'three']
#
# for enum, item in enum_generator(lst, 0):
#     print(enum, item)


## testing map_generator
# def test_func(number):
#     return number*2
# num_list = list(range_generator(0, 10))
# print(num_list)
#
# y = map_generator(test_func, num_list)
#
# print(next(y))
# print(next(y))
#
# y = map_generator(test_func, num_list)
#
# for i in y:
#     print(i)