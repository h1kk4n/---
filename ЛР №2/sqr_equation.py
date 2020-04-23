from cmath import sqrt as complex_root

def coef_split(data):
    data = data.replace(" ", "").replace("=0", "")
    degree_list = ['2', '']
    coefs = []
    for i in degree_list:
        x = data.find("x"+i)
        x_sign = max(data.rfind("-", 0, x), data.rfind("+", 0, x))
        if x_sign == -1:
            x_sign = 0
        n = data[x_sign:x]
        data = data.replace(n+"x"+i, "")
        if n == '' or n == '+' :
            n = '1'
        elif n == '-':
            n = '-1'
        coefs.append(int(n))
    coefs.append(int(data))
    return coefs


def solution_checker(a, b, c, x):
    try:
        return round(a * x ** 2 + b * x + c) == 0
    except TypeError:
        check = (a * x ** 2 + b * x + c) ** 2
        return  abs(check.real) <= 10**(-10) and abs(check.imag) <= 10**(-10)


def viete_solution(a, b, c):
    for x1 in range(c + 1):
        for x2 in range(c + 1):
            if (x1 * x2) == c and (x1 + x2) == -b:
                if x1 != x2 and solution_checker(a, b, c, x1) and solution_checker(a, b, c, x2):
                    return 'x1 = '+str(x1)+', x2 = '+str(x2)
                elif x1 == x2 and solution_checker(a, b, c, x1):
                    return 'x = '+str(x1)
                return "Что-то пошло не так, корни не прошли проверку"
    return None


def discr_solution(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
    elif discr == 0:
        x = -b / (2 * a)
        return 'x = '+str(x)
    else:
        x1 = (-b + complex_root(discr)) / (2 * a)
        x2 = (-b - complex_root(discr)) / (2 * a)
    if solution_checker(a, b, c, x1) and solution_checker(a, b, c, x2):
        return 'x1 = '+str(x1)+', x2 = '+str(x2)
    else:
        return "Что-то пошло не так, корни не прошли проверку"


def sqr_solution(a, b, c):
    if a == 1:
        solution = viete_solution(a, b, c)
    if a != 1 or solution == None:
        solution = discr_solution(a, b, c)
    return(solution)


def main():
    with open("sqr_equations.txt") as f:
        equations = f.read().split('\n')
        if equations[-1] == '':
            del equations[-1]
    for eq in equations:
        coef = coef_split(eq)
        a, b, c = coef[0], coef[1], coef[2]
        solution = sqr_solution(a, b, c)
        with open('sq_solutions.txt', 'a') as f:
            f.write('Equation: '+eq + '\nRoots: ' + solution + '\n\n')

if __name__ == "__main__":
    main()
