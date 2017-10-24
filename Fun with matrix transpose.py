matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
transposed=[]
for i in range(4):
    for row in matrix:
        #print(row)
        transposed.append(row[i])
    print(transposed)
    transposed=[]

print("\n\n\n")
matrix2=[[1, 5, 9],[2, 6, 10],[3, 7, 11],[4, 8, 12]]

for i in range(3):
    transposed.append([row[i] for row in matrix2])


print(transposed)

print("\n\n\n")


matrix3=[[1, 5, 9],[2, 6, 10],[3, 7, 11],[4, 8, 12]]

print(list(zip(*matrix3)))
