def get_magic_triangle(param):
    result=[]

    for i in range(param):
        row = []
        if i < 2:
            for j in range(i+1):
                row.append(1)
        else:
            row.append(1)
            for j in range(i-1):
                row.append(result[i-1][j]+result[i-1][j+1])
            row.append(1)
        result.append(row)
    return result


get_magic_triangle(5)	





# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]