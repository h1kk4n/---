from numpy import append, array, matmul, linspace, add, savetxt
from numpy import delete as npdel
from numpy.linalg import det
from numpy.linalg import inv as matrix_inversion

def create_row(data, var_list):
    data = data.replace(" ", "").split('=')
    data[1] = int(data[1])
    matrix_row = array([], dtype=float)
    for i in var_list:
        var = data[0].find(i)
        var_sign = max(data[0].rfind("-", 0, var), data[0].rfind("+", 0, var))
        if var_sign == -1:
            var_sign = 0
        n = data[0][var_sign:var]
        data[0] = data[0].replace(n+i, "")
        if n == '' or n == '+' :
            n = '1'
        elif n == '-':
            n = '-1'
        if var == -1:
            n = '0'
        matrix_row = append(matrix_row, int(n))
    matrix_row = append(matrix_row, data[1])
    return matrix_row

def create_matrix(filename):
    var_list = []
    with open(filename) as f:
        equations = f.read()
        for i in equations:
            if i.isalpha() and i not in var_list:
                var_list += i
        equations = equations.split('\n')
        if equations[-1] == '':
            del equations[-1]
    matrix = array([], dtype=float)
    for eq in equations:
        row = create_row(eq, var_list)
        matrix = append(matrix, row)
    return matrix.reshape(len(equations),len(row))


def split_matrix(matrix):
    B = array([], dtype=float)
    for rows in matrix:
        B = append(B, int(rows[-1]))
    A = npdel(matrix, -1, 1)
    B = B.reshape(len(matrix), 1)
    return A, B


def solution_checker(A, X, B):
    checker = matmul(A, X)
    for i in range(len(checker)):
        if abs(B[i] - checker[i]) >= 10**(-10):
            return False
    return True

# Матричный метод
def matrix_method(A, B):
    X = matmul(matrix_inversion(A), B)[:, 0]
    if solution_checker(A, X, B):
        return X
    else:
        return "Что-то пошло не так, корни не прошли проверку"

# Метод Крамера
def cramers_rule(A, B):
    det_A = det(A)
    if det_A == 0:
        return "Нет корней"
    tmp_Ai = array([], dtype=float)
    roots = array([], dtype=float)
    for i in range(len(A[0])):
        tmp_Ai = append(tmp_Ai, A).reshape(len(A), len(A[0]))
        tmp_Ai[:, i] = B[:, 0]
        det_Ai = det(tmp_Ai)
        roots = append(roots, det_Ai / det_A)
        tmp_Ai = array([], dtype=float)
    if solution_checker(A, roots, B):
        return roots
    else:
        return "Что-то пошло не так, корни не прошли проверку"

# Метод Гаусса
def gauss_elimination(matrix):
    n = len(matrix)
    init_matrix = append(array([]), matrix).reshape(len(matrix), len(matrix[0]))
    for i in range(0, n):
        max_el = abs(matrix[i, i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k, i]) > max_el:
                max_el = abs(matrix[k, i])
                max_row = k
        tmp = append(array([]), matrix[max_row, :])
        matrix[max_row, :] = matrix[i, :]
        matrix[i, :] = tmp
        for k in range(i + 1, n):
            c = -matrix[k, i] / matrix[i, i]
            matrix[k, :] = add(matrix[k, :], c * matrix[i, :])
    x = linspace(0, 0, n)
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i, n] / matrix[i, i]
        matrix[:, n] = add(matrix[:, n], -matrix[:, i] * x[i])
    if solution_checker(init_matrix[:, :len(matrix[0])-1], x, init_matrix[:, -1]):
        return x
    else:
        return "Что-то пошло не так, корни не прошли проверку"


def main():
    matrix = create_matrix("linear_equations.txt")
    A, B = split_matrix(matrix)
    with open("linear_solution.txt", "a") as f:
        savetxt(f, matrix, header="Initial extended matrix:",
                fmt="%.02f;", footer="\n", comments="")
    try:
        g_solve = gauss_elimination(matrix)
        m_solve = matrix_method(A, B)
        c_solve = cramers_rule(A, B)
        with open("linear_solution.txt", "a") as f:
            savetxt(f, g_solve, fmt="%.02f; ", header="Gaussian Elimination:\n",
                    newline="", comments="")
            savetxt(f, c_solve, fmt="%.02f; ", header="\n\nCramer's Rule:\n",
                    newline="", comments='')
            savetxt(f, m_solve, fmt="%.02f; ", header='\n\nMatrix Method:\n',
                    newline="", comments='', footer="\n\n\n\n")
    except:
        with open('linear_solution.txt', 'a') as f:
            f.write("Something has gone wrong or system has infinite amount of or no linear roots\n\n\n\n")


if __name__ == "__main__":
    main()
