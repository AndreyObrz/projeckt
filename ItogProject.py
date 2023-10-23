# Импортируем sqlite и Tkinter
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import *

# Cоздаем окно
window =  tk.Tk()

# Задаем названи окну
window.title("Сотрудники Компании") 

frame = ttk.Frame(window)

frame.pack(padx=10,pady=10)
# Создаем соедидение
conn=sqlite3.connect('company.db')

# Создаем курсос для взаимодействия с БД
cursor = conn.cursor()

# Создание таблицы
conn.execute("CREATE TABLE IF NOT EXISTS employees (fio TEXT, phone TEXT, email TEXT, salary REAL)")


# Функция добавления записи в таблицу БД
def add_employee():
    fio = fio_entry1.get()
    phone= phone_entry1.get()
    email= email_entry1.get()
    salary = salary_entry1.get()

    query_insert='''
    INSERT INTO employees (fio, phone, email, salary) 
    VALUES (?, ?, ?, ?)
    '''
    user_data=(fio,phone,email,salary)
    cursor.execute(query_insert,user_data)
    # Сохраняем изменения
    conn.commit()

# Функция  изменеия элементов таблицы БД
def update_employee():
    fio = fio_entry.get()
    phone=phone_entry.get()
    email= email_entry.get()
    salary = salary_entry.get()

    conn.execute("UPDATE employees SET phone = ?, email = ?, salary = ? WHERE fio = ?", (phone,email,salary,fio))
    conn.commit()

# Функция удаления элементов таблицы БД
def delete_employee():
    fio= delete_entry.get()


    conn.execute("DELETE FROM employees WHERE fio = ?", (fio,))
    conn.commit()


# Функция поиска по имени в таблице БД
def search_employee():

    fio=search_entry.get()
    cursor.execute("SELECT * FROM employees WHERE fio LIKE ?", ('%'+ fio + '%',))
    print(*cursor.fetchall(),sep='\n')
    print()



# Cоздание виджетов
ttk.Label(frame, text='ФИО ').grid(row=0,column=0,sticky=tk.W)

fio_entry1 = ttk.Entry(frame)

fio_entry1.grid(row=0, column = 1)



ttk.Label(frame, text='Телефон ').grid(row=1,column=0,sticky=tk.W)

phone_entry1 = ttk.Entry(frame)

phone_entry1.grid(row=1, column = 1)



ttk.Label(frame, text='Email ').grid(row=2,column=0,sticky=tk.W)

email_entry1 = ttk.Entry(frame)

email_entry1.grid(row=2, column = 1)



ttk.Label(frame, text='Заработная Плата ').grid(row=3,column=0,sticky=tk.W)

salary_entry1 = ttk.Entry(frame)

salary_entry1.grid(row=3, column = 1)


# Создание кнопки с командой запуска функции add_employee

add_button = ttk.Button(frame, text="Добавить", command=add_employee)

add_button.grid(row=4,column=1, columnspan=2, pady=10)

# Создание виджетов

ttk.Label(frame,text="ФИО Сотрудника").grid(row=5,column=0, sticky=tk.W)

fio_entry= ttk.Entry(frame)

fio_entry.grid(row=5, column=1)


ttk.Label(frame, text = "Новый Телефон").grid(row=6, column=0, sticky=tk.W)

phone_entry = ttk.Entry(frame)

phone_entry.grid(row=6,column=1)


ttk.Label(frame, text= "Новый Email").grid(row=7, column=0, sticky=tk.W)

email_entry = ttk.Entry(frame)

email_entry.grid(row=7,column=1)



ttk.Label(frame,text="Новая Заработная плата ").grid(row=8, column=0, sticky=tk.W)

salary_entry = ttk.Entry(frame)

salary_entry.grid(row=8, column=1)

# Создание кнопки с командой запуска функции update_employee

update_button = ttk.Button(frame, text =" Изменить", command = update_employee)

update_button.grid(row=10, column=1)

# Создание виджета

ttk.Label(frame,text="ФИО, которое требуется удалить").grid(row=11, column=0, sticky=tk.W)

delete_entry = ttk.Entry(frame)

delete_entry.grid(row=11, column=1)


# Создание кнопки с командой запуска функции delete_employee

delete_button = ttk.Button(frame, text= "Удалить", command=delete_employee)

delete_button.grid(row=12, column =1, columnspan=2, pady=10)


# Создание виджета


ttk.Label(frame, text= "Введите ФИО").grid(row=13,column = 0, sticky=tk.W)
ttk.Label(frame, text= "(Пустое выведет все)").grid(row=14,column = 0, sticky=tk.W)
search_entry= ttk.Entry(frame)

search_entry.grid(row=13, column=1)

# Создание кнопки с командой запуска функции search_employee

search_button = ttk.Button(frame, text="Найти", command= search_employee)

search_button.grid(row=15, column= 1, columnspan= 2, pady=10)

window.mainloop()

conn.close()




