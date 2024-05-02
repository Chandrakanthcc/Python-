rows = 8
cols = 8
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)  
    matrix.append(row)
    
for row in matrix:
    print(row)

