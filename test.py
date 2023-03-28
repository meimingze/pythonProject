
import math

class Solution:
    @staticmethod
    def solveByGauss(n, matrix):
        # 初始化
        for i in range(n):
            matrix[i] = [matrix[i][j] for j in range(n + 1)]
        isSolutionExists = True
        errorMessage = ""

        # 高斯主元消元
        for i in range(n):
            maxElementRow = i
            maxElement = abs(matrix[i][i])
            for j in range(i + 1, n):
                if abs(matrix[j][i]) > maxElement:
                    maxElementRow = j
                    maxElement = abs(matrix[j][i])
            if maxElement == 0:
                isSolutionExists = False
                errorMessage = "The system has no roots of equations or has an infinite set of them."
                break
            if maxElementRow != i:
                matrix[i], matrix[maxElementRow] = matrix[maxElementRow], matrix[i]
            for j in range(i + 1, n):
                coef = -matrix[j][i] / matrix[i][i]
                for k in range(i + 1, n + 1):
                    matrix[j][k] += coef * matrix[i][k]
                matrix[j][i] = 0

        # 回代求解
        result = [0] * n
        for i in range(n - 1, -1, -1):
            s = 0
            for j in range(i + 1, n):
                s += matrix[i][j] * result[j]
            result[i] = (matrix[i][n] - s) / matrix[i][i]

        # 计算残差
        residual_errors = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += matrix[i][j] * result[j]
            residual_errors[i] = abs(matrix[i][n] - s)

        if isSolutionExists:
            return [matrix, *result, *residual_errors]
        else:
            return [errorMessage]

if __name__ == '__main__':
    n = int(input().strip())

    matrix_rows = n
    matrix_columns = n + 1

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))

    result = Solution.solveByGauss(n, matrix)
    if Solution.isSolutionExists:
        print('\n'.join(map(str, result)))
    else:
        print(f"{Solution.errorMessage}\n")
    print('\n')