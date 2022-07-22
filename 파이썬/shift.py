data = 100
result = 0


for i in range(1, 3):
    result = data >> i
    result = result + 1

print(result)


# 0110 0100 100
# 0011 0010 50
# 0001 1001 25
