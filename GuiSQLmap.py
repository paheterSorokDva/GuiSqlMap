import tkinter.commondialog

import customtkinter
import os



class Frame0(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)



        # Опишу тока один фрейм так, как одни и те же фреймы ниже
        # Где-то колонки разные для выравнивания так как это было быстрее
        # колоночки горизонтально
        self.grid_columnconfigure((0,1,2,3), weight=1)
        # колоночки вертикально
        self.grid_rowconfigure((0,1,2,3), weight=1)



        # row 0
        self.label = customtkinter.CTkLabel(self, text = "Site:")    # названия ввода поля
        self.label.grid(row=0, column=0, padx=0, pady = 1)



        self.entry = customtkinter.CTkEntry(self, placeholder_text="Site", width= 300,height=30) # Сам инпут
        self.entry.grid(row=0, column=1, padx=0, pady = 1)



        # row 1
        def button_funtion():
            App.textFram0 = self.entry.get()
            if App.textFram0 == "":
                tkinter.messagebox.showerror("Error", "None SITE") # Визуальное сообщение
            else:
                os.system('python3 sqlmap.py -u ' + App.textFram0 + ' --dbs') #Аргументы для запуска
                #print('python3 sqlmap.py -u ' + App.textFram0 + ' --dbs')  # Аргументы для запуска

        self.button = customtkinter.CTkButton(master = self, text="Get DB", command=button_funtion)
        self.button.grid(row=1, column=1, padx=0, pady=0)

class Frame1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0, 1, 2, 3,4,5), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # row 0
        self.label = customtkinter.CTkLabel(self, text = "Tables:")
        self.label.grid(row=0, column=0, padx=0, pady = 1)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Tables", width= 300,height=30)
        self.entry.grid(row=0, column=1, padx=0, pady = 1)

        # row 1
        def button_funtion():
            App.textFram1 = self.entry.get()
            if App.textFram1 == "" and App.textFram0 == "":
                tkinter.messagebox.showerror("Error", "None Site and Tables")
            elif App.textFram1 == "" or App.textFram0 == "":
                tkinter.messagebox.showerror("Error", "ERROR SITE OR TABLES")
            else:
                os.system('python3 sqlmap.py -u ' + App.textFram0 + ' -D ' + App.textFram1 + ' --tables') #Аргументы для запуска
                #print('python3 sqlmap.py -u ' + App.textFram0 + ' -D ' + App.textFram1 + ' --tables')  # Аргументы для запуска
        self.button = customtkinter.CTkButton(self, text="Get Tables", command= button_funtion)
        self.button.grid(row=1, column=1, padx=0, pady=0)

class Frame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0, 1, 2, 3,4,5,6,7), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # row 0
        self.label = customtkinter.CTkLabel(self, text = "Columns:")
        self.label.grid(row=0, column=0, padx=0, pady = 1)

        self.entry = customtkinter.CTkEntry(self, width= 300,height=30, placeholder_text="Columns")
        self.entry.grid(row=0, column=1, padx=0, pady = 1)

        # row 1
        def button_funtion():
            App.textFram2 = self.entry.get()
            if App.textFram1 == "" and App.textFram0 == "" and App.textFram2 == "":
                tkinter.messagebox.showerror("Error", "None Site and Tables and Columns")
            elif App.textFram1 == "" or App.textFram0 == "" or App.textFram2 == "":
                tkinter.messagebox.showerror("Error", "ERROR SITE OR TABLES")
            else:
                os.system('python3 sqlmap.py -u ' + App.textFram0 + ' -D ' + App.textFram1 + ' -T ' + App.textFram2 + ' --columns') #Аргументы для запуска
                #print('python3 sqlmap.py -u ' + App.textFram0 + ' -D ' + App.textFram1 + ' -T ' + App.textFram2 + ' --columns')  # Аргументы для запуска
        self.button = customtkinter.CTkButton(self, text="Get Columns", command= button_funtion)
        self.button.grid(row=1, column=1, padx=0, pady=0)

class Frame3(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0, 1, 2, 3,4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)



        # row 0
        self.label = customtkinter.CTkLabel(self, text = "Dump:")
        self.label.grid(row=0, column=0, padx=0, pady = 1)

        self.entry = customtkinter.CTkEntry(self, width= 300,height=30, placeholder_text="Dump")
        self.entry.grid(row=0, column=1, padx=0, pady = 1)

        # row 1
        def button_funtion():
            App.textFram3 = self.entry.get()
            if App.textFram1 == "" and App.textFram0 == "" and App.textFram2 == "" and App.textFram3 == "":
                tkinter.messagebox.showerror("Error", "None Site and Tables and columns and Dump")
            elif App.textFram1 == "" or App.textFram0 == "" or App.textFram2 == "" or App.textFram3 == "":
                tkinter.messagebox.showerror("Error", "ERROR SITE OR TABLES OR COLUMNS")
            else:
                os.system('python3 sqlmap.py -u ' + App.textFram0 + ' -D ' + App.textFram1 + ' -T ' + App.textFram2 + ' -C ' + App.textFram3 + ' --dump') #Аргументы для запуска
                #print('python3 sqlmap.py -u ' + App.textFram0 + ' -D ' + App.textFram1 + ' -T ' + App.textFram2 + ' -C ' + App.textFram3 + ' --dump')  # Аргументы для запуска
        self.button = customtkinter.CTkButton(self, text="Dump", command= button_funtion)
        self.button.grid(row=1, column=1, padx=0, pady=0)

class Frame4(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        customtkinter.set_default_color_theme("green") # меняем на зеленую


        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)



        # row 0
        self.label = customtkinter.CTkLabel(self, text = "GOOGLE DORKS")
        self.label.grid(row=0, column=1, padx=0)

        self.entry = customtkinter.CTkEntry(self, width= 200,height=30)
        self.entry.grid(row=1, column=1, padx=0)

        # row 1

        def button_funtion():
            App.textFram4 = self.entry.get()
            if App.textFram4 == "":
                tkinter.messagebox.showinfo("Info", "Pysto")
            else:
                os.system('python3 sqlmap.py -g ' + App.textFram4 ) #Аргументы для запуска
                #print('python3 sqlmap.py -g ' + App.textFram4)  # Аргументы для запуска

        self.button = customtkinter.CTkButton(self, text="Search", command= button_funtion)
        self.button.grid(row=2, column=1, padx=0, pady=0,)

class App(customtkinter.CTk):
    textFram0 = ""
    textFram1 = ""
    textFram2 = ""
    textFram3 = ""
    textFram4 = ""

    def __init__(self):
        super().__init__()

        # Ебашим темную тему
        customtkinter.set_appearance_mode("system") # Тема
        customtkinter.set_default_color_theme("blue") # Тема кнопочек и не только

        self.wm_iconbitmap("sql2.ico")




        # Название
        self.title("SqlMap (paheterGUI)")

        #self.geometry("400x180") #Можно и это использовать

        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=2)

        # Блокируем окошко
        self.minsize(width= 480, height= 820)
        self.maxsize(width= 480, height= 820)

        # row 0
        self.frame0 = Frame0(master=self)

        self.frame0.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        # row 1
        self.frame1 = Frame1(master=self)
        self.frame1.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        # row 2
        self.frame2 = Frame2(master=self)
        self.frame2.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        # row 3
        self.frame3 = Frame3(master=self)
        self.frame3.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        # row 4
        self.frame4 = Frame4(master=self)
        self.frame4.grid(row=4, column=0, padx=20, pady=20, sticky="nsew")



app = App()
#os.system('python3 sqlmap.py --update') # обновляем перед запуском
app.mainloop()
