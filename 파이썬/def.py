from unittest import result


x = 10
y = 20
z = 30
h = "hello"
w = "world"


def add(x, y, z):
    result = x + y + z
    return result


print(add)
print(add(x, y, z))


start = h.upper() + w.upper()
print(start)
