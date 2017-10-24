squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)
squares3 = [x**2 for x in range(10)]
print(squares3)
