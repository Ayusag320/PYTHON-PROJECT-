from tkinter import *
import tkinter.font as font
import random
import tkinter as tk
import math
import string
from tkinter import messagebox
import sqlite3 as sql



root = Tk()
root.title("MY PROJECT - ")
app_font = font.Font(size = 12)
root.config(bg = '#66CDAA')
# WINDOW COLOR
root.geometry('650x300')

player_score = 0
computer_score = 0
options = [('calculator', 0), ('todolist', 1),('snake',2)]

Label(text = 'SELECT ONE ', font = font.Font(size = 20),fg = 'BLACK', bg = '#808A87').pack()


def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    if player_input == options[0]:
        root = tk.Tk()
        root.title('My Scientific Calculator')
        root.configure(bg='#696969')
        root.resizable(width=False, height=False)

        ent_field = tk.Entry(root, bg='#D3D3D3', fg='#0F0F0F', font=('Verdana', 35),
                             borderwidth=1, justify="right")
        ent_field.grid(row=0, columnspan=15, padx=15, pady=15,
                       sticky='n' + 's' + 'e' + 'w')
        ent_field.insert(0, '00')

        FONT = ('Verdana', 14, 'bold')

        class SC_Calculator():
            def __init__(self):
                self.current = ''
                self.inp_value = True
                self.result = False

            def Entry(self, value):
                ent_field.delete(0, 'end')
                ent_field.insert(0, value)

            def Enter_Num(self, num):
                self.result = False
                firstnum = ent_field.get()
                secondnum = str(num)
                if self.inp_value:
                    self.current = secondnum
                    self.inp_value = False
                else:
                    self.current = firstnum + secondnum
                self.Entry(self.current)

            def Standard_Ops(self, val):
                temp_str = ent_field.get()
                try:
                    if val == '=':
                        ans = str(eval(temp_str))
                        self.result = True
                        self.Entry(ans)
                    else:
                        self.Entry(temp_str + val)
                    self.inp_value = False
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Clear_Entry(self):
                self.result = False
                self.current = "0"
                self.Entry(0)
                self.inp_value = True

            def SQ_Root(self):
                try:
                    self.current = math.sqrt(float(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Pi(self):
                self.result = False
                self.current = math.pi
                self.Entry(self.current)

            def E(self):
                self.result = False
                self.current = math.e
                self.Entry(self.current)

            def Deg(self):
                try:
                    self.result = False
                    self.current = math.degrees(float(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Rad(self):
                try:
                    self.result = False
                    self.current = math.radians(float(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Exp(self):
                try:
                    self.result = False
                    self.current = math.exp(float(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Fact(self):
                try:
                    self.result = False
                    self.current = math.factorial(float(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Sin(self):
                try:
                    self.result = False
                    self.current = math.sin(math.radians(float(ent_field.get())))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Cos(self):
                try:
                    self.result = False
                    self.current = math.cos(math.radians(float(ent_field.get())))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Tan(self):
                try:
                    self.result = False
                    self.current = math.tan(math.radians(float(ent_field.get())))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Sinh(self):
                try:
                    self.result = False
                    self.current = math.sinh(math.radians(float(ent_field.get())))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Cosh(self):
                try:
                    self.result = False
                    self.current = math.cosh(math.radians(float(ent_field.get())))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Tanh(self):
                try:
                    self.result = False
                    self.current = math.tanh(math.radians(float(ent_field.get())))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Ln(self):
                try:
                    self.result = False
                    self.current = math.log(float(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Log_10(self):
                try:
                    self.result = False
                    self.current = math.log10(float(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Log_2(self):
                try:
                    self.result = False
                    self.current = math.log2(float(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Pow_2(self):
                try:
                    self.result = False
                    self.current = int(ent_field.get()) ** 2
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Pow_3(self):
                try:
                    self.result = False
                    self.current = int(ent_field.get()) ** 3
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Pow_10_n(self):
                try:
                    self.result = False
                    self.current = 10 ** int(ent_field.get())
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def One_div_x(self):
                try:
                    self.result = False
                    self.current = 1 / (int(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

            def Abs(self):
                try:
                    self.result = False
                    self.current = abs(float(ent_field.get()))
                    self.Entry(self.current)
                except ValueError:
                    self.Entry('Error')
                except SyntaxError:
                    self.Entry('Error')

        numberpad = "789456123"
        i = 0
        button = []
        for j in range(2, 5):
            for k in range(3):
                button.append(tk.Button(root, text=numberpad[i], font=FONT,
                                        fg="blue4", width=7, height=2,
                                        highlightbackground='#8b5f65', highlightthickness=5))
                button[i].grid(row=j, column=k, sticky='n' +
                                                       's' + 'e' + 'w', padx=10, pady=10)
                button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
                i += 1

        btn_CE = tk.Button(root, text='CLEAR', command=lambda: sc_app.Clear_Entry(),
                           font=FONT, height=3, fg="#B22222",
                           highlightbackground='#ADD8E6', highlightthickness=5)
        btn_CE.grid(row=1, column=0, columnspan=2,
                    sticky='n' + 's' + 'e' + 'w', padx=8, pady=8)

        btn_sqr = tk.Button(root, text='\u221A', command=lambda: sc_app.SQ_Root(),
                            font=FONT, width=6, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_sqr.grid(row=1, column=2, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_0 = tk.Button(root, text='0', command=lambda: sc_app.Enter_Num('0'),
                          font=FONT, width=6, height=2, fg="#000000",
                          highlightbackground='#ADD8E6', highlightthickness=2)
        btn_0.grid(row=5, column=0, columnspan=2,
                   sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_point = tk.Button(root, text='.', command=lambda: sc_app.Standard_Ops('.'),
                              font=FONT, width=6, height=2, fg="#000000",
                              highlightbackground='#ADD8E6', highlightthickness=2)
        btn_point.grid(row=5, column=2, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_equal = tk.Button(root, text='=', command=lambda: sc_app.Standard_Ops('='),
                              font=FONT, width=6, height=2, fg="#000000",
                              highlightbackground='#ADD8E6', highlightthickness=2)
        btn_equal.grid(row=5, column=3, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_add = tk.Button(root, text='+', command=lambda: sc_app.Standard_Ops('+'),
                            font=FONT, width=6, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_add.grid(row=1, column=3, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_sub = tk.Button(root, text='-', command=lambda: sc_app.Standard_Ops('-'),
                            font=FONT, width=6, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_sub.grid(row=2, column=3, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_mul = tk.Button(root, text='*', command=lambda: sc_app.Standard_Ops('*'),
                            font=FONT, width=6, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_mul.grid(row=3, column=3, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_div = tk.Button(root, text='/', command=lambda: sc_app.Standard_Ops('/'),
                            font=FONT, width=6, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_div.grid(row=4, column=3, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_pi = tk.Button(root, text='\u03C0', command=lambda: sc_app.Pi(),
                           font=FONT, width=5, height=2, fg="#000000",
                           highlightbackground='#ADD8E6', highlightthickness=2)
        btn_pi.grid(row=1, column=4, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_e = tk.Button(root, text='e', command=lambda: sc_app.E(),
                          font=FONT, width=5, height=2, fg="#000000",
                          highlightbackground='#ADD8E6', highlightthickness=2)
        btn_e.grid(row=1, column=5, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_deg = tk.Button(root, text='Deg', command=lambda: sc_app.Deg(),
                            font=FONT, width=5, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_deg.grid(row=1, column=6, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_exp = tk.Button(root, text='Exp', command=lambda: sc_app.Exp(),
                            font=FONT, width=5, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_exp.grid(row=2, column=4, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_fact = tk.Button(root, text='x!', command=lambda: sc_app.Fact(),
                             font=FONT, width=5, height=2, fg="#000000",
                             highlightbackground='#ADD8E6', highlightthickness=2)
        btn_fact.grid(row=2, column=5, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_rad = tk.Button(root, text='Rad', command=lambda: sc_app.Rad(),
                            font=FONT, width=5, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_rad.grid(row=2, column=6, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_sin = tk.Button(root, text='sin', command=lambda: sc_app.Sin(),
                            font=FONT, width=5, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_sin.grid(row=3, column=4, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_cos = tk.Button(root, text='cos', command=lambda: sc_app.Cos(),
                            font=FONT, width=5, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_cos.grid(row=3, column=5, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_tan = tk.Button(root, text='tan', command=lambda: sc_app.Tan(),
                            font=FONT, width=5, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_tan.grid(row=3, column=6, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_sinh = tk.Button(root, text='sinh', command=lambda: sc_app.Sinh(),
                             font=FONT, width=5, height=2, fg="#000000",
                             highlightbackground='#ADD8E6', highlightthickness=2)
        btn_sinh.grid(row=4, column=4, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_cosh = tk.Button(root, text='cosh', command=lambda: sc_app.Cosh(),
                             font=FONT, width=5, height=2, fg="#000000",
                             highlightbackground='#ADD8E6', highlightthickness=2)
        btn_cosh.grid(row=4, column=5, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_tanh = tk.Button(root, text='tanh', command=lambda: sc_app.Tanh(),
                             font=FONT, width=5, height=2, fg="#000000",
                             highlightbackground='#ADD8E6', highlightthickness=2)
        btn_tanh.grid(row=4, column=6, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_ln = tk.Button(root, text='ln', command=lambda: sc_app.Ln(),
                           font=FONT, width=5, height=2, fg="#000000",
                           highlightbackground='#ADD8E6', highlightthickness=2)
        btn_ln.grid(row=5, column=4, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_log2 = tk.Button(root, text='log2', command=lambda: sc_app.Log_2(),
                             font=FONT, width=5, height=2, fg="#000000",
                             highlightbackground='#ADD8E6', highlightthickness=2)
        btn_log2.grid(row=5, column=5, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_x_pow2 = tk.Button(root, text='x\u00B2', command=lambda: sc_app.Pow_2(),
                               font=FONT, width=5, height=2, fg="#000000",
                               highlightbackground='#ADD8E6', highlightthickness=2)
        btn_x_pow2.grid(row=1, column=7, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_x_pow3 = tk.Button(root, text='x\u00B3', command=lambda: sc_app.Pow_3(),
                               font=FONT, width=5, height=2, fg="#000000",
                               highlightbackground='#ADD8E6', highlightthickness=2)
        btn_x_pow3.grid(row=2, column=7, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_10_pow_n = tk.Button(root, text='10\u207F', command=lambda: sc_app.Pow_10_n(),
                                 font=FONT, width=5, height=2, fg="#000000",
                                 highlightbackground='#ADD8E6', highlightthickness=2)
        btn_10_pow_n.grid(row=3, column=7, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_1div_by_x = tk.Button(root, text='1/x', command=lambda: sc_app.One_div_x(),
                                  font=FONT, width=5, height=2, fg="#000000",
                                  highlightbackground='#ADD8E6', highlightthickness=2)
        btn_1div_by_x.grid(row=4, column=7, sticky='n' + 's' + 'e' + 'w', padx=10, pady=10)

        btn_abs = tk.Button(root, text='MADE BY - AYUSH GUPTA',
                            font=('Jacaranda', 10, 'bold'), width=15, height=2, fg="#000000",
                            highlightbackground='#ADD8E6', highlightthickness=2)
        btn_abs.grid(row=5, column=6, columnspan=2, sticky='n' + 's' + 'e' + 'w', padx=3, pady=17)

        if __name__ == '__main__':
            sc_app = SC_Calculator()

            root.mainloop()


    elif player_input == options[1]:

        from tkinter import messagebox
        import sqlite3 as sql

        def add_task():
            task_string = task_field.get()
            if len(task_string) == 0:
                messagebox.showinfo('Error', 'Field is Empty.')
            else:
                tasks.append(task_string)
                the_cursor.execute('insert into tasks values (?)', (task_string,))
                list_update()
                task_field.delete(0, 'end')

        def list_update():
            clear_list()
            for task in tasks:
                task_listbox.insert('end', task)

        def delete_task():
            try:
                the_value = task_listbox.get(task_listbox.curselection())
                if the_value in tasks:
                    tasks.remove(the_value)
                    list_update()
                    the_cursor.execute('delete from tasks where title = ?', (the_value,))
            except:
                messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

        def delete_all_tasks():
            message_box = messagebox.askyesno('Delete All', 'Are you sure?')
            if message_box == True:
                while (len(tasks) != 0):
                    tasks.pop()
                the_cursor.execute('delete from tasks')
                list_update()

        def clear_list():
            task_listbox.delete(0, 'end')

        def close():
            print(tasks)
            guiWindow.destroy()

        def retrieve_database():
            while (len(tasks) != 0):
                tasks.pop()
            for row in the_cursor.execute('select title from tasks'):
                tasks.append(row[0])

        if __name__ == "__main__":
            guiWindow = Tk()
            guiWindow.title("Your-To-Do List ")
            guiWindow.geometry("700x400+550+250")
            guiWindow.resizable(0, 0)
            guiWindow.configure(bg="#D3D3D3")

            the_connection = sql.connect('listOfTasks.db')
            the_cursor = the_connection.cursor()
            the_cursor.execute('create table if not exists tasks (title text)')

            tasks = []

            functions_frame = Frame(guiWindow, bg="#696969")

            functions_frame.pack(side="top", expand=True, fill="both")

            task_label = Label(functions_frame, text="TO-DO-LIST \n Enter the Task Title:",
                               font=("CORAL", "11", "bold"),
                               background="#8B5F65",
                               foreground="#000000"
                               )
            task_label.place(x=20, y=25)

            task_field = Entry(
                functions_frame,
                font=("CORAL", "14"),
                width=42,
                foreground="black",
                background="GRAY79",
            )
            task_field.place(x=189, y=30)

            add_button = Button(
                functions_frame,
                text="Add..",
                width=15,
                bg='#8B5F65', font=("arial", "14", "bold"),
                command=add_task,

            )
            del_button = Button(
                functions_frame,
                text="Remove..",
                width=15,
                bg='#8B5F65', font=("arial", "14", "bold"),
                command=delete_task,
            )
            del_all_button = Button(
                functions_frame,
                text="Delete All..",
                width=15,
                font=("arial", "14", "bold"),
                bg='#8B5F65',
                command=delete_all_tasks
            )

            exit_button = Button(
                functions_frame,
                text="Exit / Close..",
                width=52,
                bg='#8B5F65', font=("PINE", "14", "bold"),
                command=close
            )

            name_button = Button(
                functions_frame,
                text="MADE BY - AYUSH GUPTA",
                width=44,
                bg='#696969', font=("PINE", "14", "bold"),

            )

            add_button.place(x=20, y=80)
            del_button.place(x=240, y=80)
            del_all_button.place(x=460, y=80)
            exit_button.place(x=15, y=330)
            name_button.place(x=70, y=370)

            task_listbox = Listbox(
                functions_frame,
                width=60,
                height=10,
                font="BOLD",
                selectmode='SINGLE',
                background="gray15",
                foreground="WHITE",
                selectbackground="#000000",
                selectforeground="BLACK"
            )
            task_listbox.place(x=27, y=140)

            retrieve_database()
            list_update()
            guiWindow.mainloop()
            the_connection.commit()
            the_cursor.close()


def get_computer_choice():
    return random.choice(options)

input_frame = Frame(root, bg = '#458B74')
input_frame.pack()

player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'BLACK', bg = '#808A87')
player_options.grid(row = 0, column = 0, pady =9)

calculator = Button(input_frame, text = 'CALCULATOR', width = 22, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[0]))
calculator.grid(row = 1, column = 1, padx = 8, pady = 5)

todolist = Button(input_frame, text = 'TO-DO-LIST', width = 22, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[1]))
todolist.grid(row = 4, column = 1, padx = 8, pady = 5)

name = Button(input_frame, text = 'MADE BY -  AYUSH GUPTA', width = 40, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[2]))
name.grid(row = 10, column = 9, padx = 5, pady = 2)

root.mainloop()
