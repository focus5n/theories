a = "Hello"
b = "World"
hello = ["Hello", ", ", "World", "!"]
diff = ["String", 1, True, ["Hello", ", ", "Hell", "!"], hello]
user = {}
user['age'] = 30
user['age'] = 35
user['name'] = 'hans'
user[1] = 'coco'
fruits = {}
fruits['color'] = ['red', 'blue']
fruits['size'] = ['10cm', 20]

print(a + ", " + b)
print(hello[1])
print(diff)
print(user[1])
print(user.get('age'))
print(fruits.get('size'))
