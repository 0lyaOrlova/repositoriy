from pickle import loads, dumps

s = {'Иван': 24, 'Сергей': 11}
d = dumps(s)
print(d)
print(loads(d))