# SOME EXERCISES 
from functools import lru_cache
from test import testEqual
from pythonds.basic import Stack

@lru_cache(maxsize=300)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

obj = Point(1, 2)
print(obj.__repr__())


def revstring(mystr):
    my_stack = Stack()
    for letter in mystr:
        my_stack.push(letter)
    revstr = ''
    while not my_stack.isEmpty():
        revstr = revstr + my_stack.peek
    return revstr
    

revstring('apple'),'elppa'
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')


