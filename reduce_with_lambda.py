from functools import reduce

lists = [2,3,4,5,6,7,8,9]

product = reduce(lambda x, y: x*y,lists)

print(product)
