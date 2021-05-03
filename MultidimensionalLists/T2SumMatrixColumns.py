def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    (rows_count,columns_count)=map(int, input().split(', '))
    matrix=[]
    for r in range(rows_count):
        row=[int(x) for x in input().split(' ')]
        matrix.append(row)
    return matrix

def get_colums_sums(matrix):
    rows_count=len(matrix)
    columns_count=len(matrix[0])
    # sums=[]
    # for column_index in range(columns_count):
    #     column_sum=0
    #     for row_index in range(rows_count):
    #         column_sum+=matrix[row_index][column_index]
    #     sums.append(column_sum)
    #
    # return sum
    # alternativno reshenie
    sums=[0]*columns_count
    for row_index in range(rows_count):
        for column_index in range (columns_count):
            sums[column_index]+=matrix[row_index][column_index]
    return sums


def print_result(values):
    [print(x) for x in values]


matrix=read_matrix(is_test=False)
result=get_colums_sums(matrix)
print_result(result)
# todo judge