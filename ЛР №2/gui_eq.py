import tkinter as tk
from sqr_equation import sqr_solution



def main():

    def kaef(event):
        a = int(textbox1.get())
        b = int(textbox2.get())
        c = int(textbox3.get())
        print(sqr_solution(a, b, c))


    root = tk.Tk()
    root.title("Лабораторная работа №2")
    root.geometry("640x480")

    textbox1 = tk.Entry(root, width=3, justify=tk.RIGHT)
    textbox1.grid(row=0, column=0)
    label1 = tk.Label(root, text="x2+")
    label1.grid(row=0, column=1)
    textbox2 = tk.Entry(root, width=3, justify=tk.RIGHT)
    textbox2.grid(row=0, column=2)
    label2 = tk.Label(root, text="x+")
    label2.grid(row=0, column=3)
    textbox3 = tk.Entry(root, width=3, justify=tk.RIGHT)
    textbox3.grid(row=0, column=4)
    label2 = tk.Label(root, text="=0")
    label2.grid(row=0, column=5)

    button1 = tk.Button(root, text="Разбить на коэффициенты")
    button1.bind('<Button-1>', kaef)
    button1.grid(row=1, columnspan="10")





    root.resizable(False, False)



    root.mainloop()

if __name__ == "__main__":
    main()
