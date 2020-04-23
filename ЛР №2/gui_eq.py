import tkinter as tk
from numpy import array
from sqr_equation import sqr_solution
from linear_equations import split_matrix, gauss_elimination
from linear_equations import matrix_method, cramers_rule


def sqr_equation(event):

    def solve_eq(event):
        a = int(tb_lst[0].get())
        b = int(tb_lst[1].get())
        c = int(tb_lst[2].get())
        solution_label['text'] = '\n'. join(sqr_solution(a, b, c).split(', '))


    sqr_w = tk.Tk()
    sqr_w.title("Решение квадратных уравнений")

    sqr_text = ["x2 +", "x +", "= 0"]
    tb_lst = []

    for i in range(3):
        coef = tk.Entry(sqr_w, width=3, justify=tk.RIGHT, font="Roboto")
        coef.grid(row=0, column=10+(i*2), pady=10)
        tb_lst.append(coef)
        eq_part = tk.Label(sqr_w, text=sqr_text[i], font="Roboto")
        eq_part.grid(row=0, column=11+(i*2), pady=10)

    solve_btn = tk.Button(sqr_w, text="Получить решение", font="Roboto")
    solve_btn.bind('<Button-1>', solve_eq)
    solve_btn.grid(row=1, columnspan=26, pady=20)

    solution_label = tk.Label(sqr_w, bg="lightgrey", fg='black', height=3,
                                width=45, font="Roboto")
    solution_label.grid(row=2, columnspan=26, pady=10)

    sqr_w.resizable(False, False)


def lin_equation(event, a, b):
    var_lst = ["x +", "y +", "z +", "w +"]
    var_lst[b-2] = var_lst[b-2].replace(var_lst[b-2][-1], '=')
    tb_lst = []

    def solve_eq(event):
        coefs = []
        for i in tb_lst:
            coefs.append(int(i.get()))
        coefs = array(coefs, dtype=float).reshape(a, b)
        A, B = split_matrix(coefs)
        g_solve = gauss_elimination(coefs)
        m_solve = matrix_method(A, B)
        c_solve = cramers_rule(A, B)
        solution_label['text'] = '\n'. join([
            "Метод Гаусса:  " + str(g_solve).replace('[ ', '').replace(']', ''),
            "Метод Крамера:  " + str(m_solve).replace('[ ', '').replace(']', ''),
            "Матричный метод:  " + str(c_solve).replace('[ ', '').replace(']', '')])


    lin_w = tk.Tk()
    lin_w.title("Решение СЛАУ")

    for i in range(a):
        for j in range(b):
            coef = tk.Entry(lin_w, width=3, justify=tk.RIGHT, font="Roboto")
            coef.grid(row=i, column=10+(j*2), pady=10)
            tb_lst.append(coef)
            if j != b - 1:
                eq_part = tk.Label(lin_w, text=var_lst[j], font="Roboto")
                eq_part.grid(row=i, column=11+(j*2), pady=10)

    solve_btn = tk.Button(lin_w, text="Получить решение", font="Roboto")
    solve_btn.bind('<Button-1>', solve_eq)
    solve_btn.grid(row=a, columnspan=26, pady=20)

    solution_label = tk.Label(lin_w, bg="lightgrey", fg='black', height=8,
                                width=60, font="Roboto")
    solution_label.grid(row=a+1, columnspan=26, pady=10)

    lin_w.resizable(False, False)


def main():
    root = tk.Tk()
    root.title("Лабораторная работа №2")

    sqr_btn = tk.Button(root, text="Решить квадратное уравнение", font="Roboto")
    sqr_btn.bind('<Button-1>', sqr_equation)
    sqr_btn.grid(row=0, column=0, padx=50, pady=20, ipadx=20, ipady=10)

    lin3_btn = tk.Button(root, text="Решить СЛАУ 3-го порядка", font="Roboto")
    lin3_btn.bind('<Button-1>', lambda event, a = 3, b = 4: lin_equation(event, a, b))
    lin3_btn.grid(row=1, column=0, padx=50, pady=20, ipadx=20, ipady=10)

    lin4_btn = tk.Button(root, text="Решить СЛАУ 4-го порядка", font="Roboto")
    lin4_btn.bind('<Button-1>', lambda event, a = 4, b = 5: lin_equation(event, a, b))
    lin4_btn.grid(row=2, column=0, padx=50, pady=20, ipadx=20, ipady=10)

    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
