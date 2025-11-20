# 练习6：打印杨辉三角。
def print_yanghui(high=4):
    weight = 2 * high - 1

    # 初始化矩阵
    matrix = [[" " for _ in range(weight)] for _ in range(high)]

    # 放入边界
    for i in range(high):
        for j in range(weight):
            if ((j <= (high-1) and j+i == high-1) or (j > (high-1) and i == j - (high-1))):
                matrix[i][j] = 1
    # 计算三角
    for i in range(1, high):
        for j in range(1, weight-1):
            if (matrix[i-1][j-1] != " " and matrix[i-1][j+1] != " "):
                matrix[i][j] = matrix[i-1][j-1]+matrix[i-1][j+1]

    print_matrix(matrix)


def print_matrix(matrix):
    for rows in matrix:
        for row in rows:
            print(row, end=" ")
        print()
    print()


print_yanghui(5)
