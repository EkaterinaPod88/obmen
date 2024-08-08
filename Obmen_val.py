import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):#функция обновления метки,event  потому что вызывам в функции комбобоx силейт
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)


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
                c_name = cur[code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {c_name} за 1 доллар")#выводим пользователю
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")#ессли код валюты не найден выводим предупреждение
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")#обрабатываем исключения
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")#


cur = {'RUB':'Российский рубль',
       'EUR':'Евро',
       'GBP':'Британский фунт стерлингов',
       'JPY':'Японская йена',
       'CNY':'Китайский юань',
       'KZT':'Казахский тенге',
       'UZS':'Узбекский сум',
       'CHF':'Швейцарский франк',
       'AED':'Дирхам ОАЭ',
       'CAD':'Канадский доллар'
       }


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Выберите код валюты").pack(padx=10, pady=10)

#cur = ['RUB','RUR','GBP','JPY','CNY','KZT','UZS','CHF','AED','CAD']

combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)


#entry = Entry()
#entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллору", command=exchange).pack(padx=10, pady=10)

window.mainloop()