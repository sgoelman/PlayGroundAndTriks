import time


class Animal():
    def __init__(self, row, col, name):
        print(name, ' row=', row, 'col=', col)


def cats():
    for i in range(2, 8):
        yield Animal(row=i, col=i, name='cat')


def mouse():
    for i in range(7, 1, -1):
        yield Animal(row=i, col=i,name=mouse)


mouse = Animal(row=7, col=7,name=mouse)

for cat in cats():
    time.sleep(.4)
