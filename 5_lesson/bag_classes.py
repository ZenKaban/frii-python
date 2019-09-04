class Container:
    def __init__(self, new_size):
        self.max_size = new_size
        self.cur_size = 0
        self.objects = []
        # fact_size = len(self.objects, )
    def add(self, new_object):
        if new_object.size >= (self.max_size - self.cur_size):
            raise Exception("{} is too big".format(new_object.name))
        else:
            self.objects.append(new_object)
            self.cur_size = self.cur_size + new_object.size
            
            print(new_object.name, "is added")

class Item:
    def __init__(self, new_item_size, name):
        self.size = new_item_size
        self.name = name

bag = Container(5)
basket = Container(3)
cube = Item(2, "Cube")
huge_ball = Item(10, "Huge Ball")

bag.add(cube)
bag.add(huge_ball)