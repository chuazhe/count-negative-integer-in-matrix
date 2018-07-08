# The matrix must be sorted in ascending order. If not, the algorithm will not work properly
matrix = [[-10, -9, 0, 40],
          [-25, -15, 35, 45],
          [-12, 20, 37, 48],
          [-12, -11, 5, 8]]

# To obtain the number of row
rowCount = len(matrix)

columnCount = 0

# To obtain the number of column
for i in matrix[0]:
    columnCount += 1

a = 0
b = 0
countOfNegativeInteger = 0

while a < rowCount and b < columnCount:
    # >=0 : find the count of negative integer, less than 0
    # It can also used to find the count of integer that is less than n. For example,
    # >20 : find the count of integer that is less than or equal to 20
    if matrix[a][b] >= 0:
        a += 1
        b = 0
    else:
        countOfNegativeInteger += 1
        b += 1

print(countOfNegativeInteger)
