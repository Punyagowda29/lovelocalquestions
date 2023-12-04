def pascals_triangle(num_rows): #function difinition
    if num_rows==0: #if row is zero
        return []
    triangle=[[1]] #else initialise triangle with [[1]]
    for i in range(1, num_rows): #The new row is constructed by adding the previous element and the element before it in the previous row
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[j-1] + prev_row[j] for j in range(1, i)] + [1]
        triangle.append(new_row)
    return triangle

# input from the user
numRows = int(input("Enter the number of rows:"))

# call Pascal's Triangle
result=pascals_triangle(numRows)

# Display the result
print(result)
