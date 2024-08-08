import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def exchange():#функция обмены валюты
    #code = entry.get()#получаем из поля ввода энтри что ввел пользователь
    code = combobox.get()
    if code:
        try:
            response = requests.get('http://open.er-api.com/v6/latest/USD')#делаем запрос к сайту
            response.raise_for_status()#получаем информацию в response
            data = response.json()#раскладываем полученное в формате json  информацию в виде словаря
            if code in data['rates']:#если в дата существует введеный код
                exchange_rate = data['rates'][code]# находим знгачение
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {code} за 1 доллар")#выводим пользователю
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")#ессли код валюты не найден выводим предупреждение
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")#обрабатываем исключения
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")#


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Выберите код валюты").pack(padx=10, pady=10)

curses = ['RUB','RUR','GBP','JPY','CNY','KZT','UZS','CHF','AED','CAD']
combobox = ttk.Combobox(values=curses)
combobox.pack(padx=10, pady=10)

#entry = Entry()
#entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллору", command=exchange).pack(padx=10, pady=10)

window.mainloop()