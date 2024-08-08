import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):#функция обновления метки,event  потому что вызывам в функции комбобоx силейт
    code = t_combobox.get()
    name = cur[code]
    c_label.config(text=name)


def exchange():#функция обмены валюты
    #code = entry.get()#получаем из поля ввода энтри что ввел пользователь
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f'http://open.er-api.com/v6/latest/{b_code}')#делаем запрос к сайту
            response.raise_for_status()#получаем информацию в response
            data = response.json()#раскладываем полученное в формате json  информацию в виде словаря
            if t_code in data['rates']:#если в дата существует введеный код
                exchange_rate = data['rates'][t_code]# находим знгачение
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}")#выводим пользователю
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена")#ессли код валюты не найден выводим предупреждение
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
       'CAD':'Канадский доллар',
       'USD':'Американский доллар'
       }


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x300")


Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)


Label(text="Целевая валюта").pack(padx=10, pady=10)

#cur = ['RUB','RUR','GBP','JPY','CNY','KZT','UZS','CHF','AED','CAD']

t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)


#entry = Entry()
#entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()