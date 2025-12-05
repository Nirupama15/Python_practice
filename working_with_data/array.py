def array(r, c):
    return [[None for j in range(c)] for i in range(r)]

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))
a = array(rows, cols)
print(a)