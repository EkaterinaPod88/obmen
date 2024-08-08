import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange():#функция обмены валюты
    code = entry.get()#получаем из поля ввода энтри что ввел пользователь

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

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллору", command=exchange).pack(padx=10, pady=10)

window.mainloop()