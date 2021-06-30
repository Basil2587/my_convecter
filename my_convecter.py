import requests
from tkinter import *
import tkinter as tk
import datetime


url = 'https://api.exchangerate-api.com/v4/latest/USD'


class CurrencyConverter():

    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, output_cur, amount):
        # ограничиваем точность до 4 знаков после запятой
        amount = round(amount * self.currencies[output_cur], 4)
        return amount


class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Конвектор валют'
        self.configure(background="#856ff8")
        self.geometry("300x300")

        # Название
        self.intro_label = Label(self, text='Конвектор валют', fg='blue')
        self.intro_label.config(font=('Ubuntu', 18, 'bold'))
        self.intro_label.place(x=60, y=5)

        # Курс на сегодняшний день
        self.date_label = Label(
            self,
            text=f"1 доллар = {converter.convert('RUB',1)} RUB"
            f"\n Дата : {date}",
            relief=tk.GROOVE, borderwidth=5)
        self.date_label.place(x=60, y=50)

        self.input_cur_label = Label(
            self,
            text="Введите USD", relief=tk.GROOVE, borderwidth=5)
        self.input_cur_label.place(x=35, y=120)

        self.output_cur_label = Label(
            self,
            text="Вывод валюты RUB", relief=tk.GROOVE, borderwidth=5)
        self.output_cur_label.place(x=35, y=235)

        # Поля ввода
        valid = (self.register(self.number_only), '%d', '%P')
        self.amount_field = Entry(
            self,
            bd=3, relief=tk.RIDGE,
            justify=tk.CENTER, width=17, validate='key',
            validatecommand=valid)
        self.converted_amount_field_label = Label(
            self,
            text='', fg='black', bg='white',
            relief=tk.RIDGE, justify=tk.CENTER, width=17, borderwidth=3)
        self.amount_field.place(x=36, y=150)
        self.converted_amount_field_label.place(x=35, y=270)

        # Кнопка "Конвертировать"
        self.convert_button = Button(
            self,
            text="Конвертировать", fg="black", command=self.perform)
        self.convert_button.config(font=('Ubuntu', 14, 'bold'))
        self.convert_button.place(x=60, y=195)

    def perform(self):
        amount = float(self.amount_field.get())
        convert_amount = converter.convert('RUB', amount)
        convert_amount = round(convert_amount, 2)
        self.converted_amount_field_label.config(text=str(convert_amount))

    def number_only(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))


if __name__ == '__main__':
    converter = CurrencyConverter(url)
    date_f = datetime.datetime.strptime(converter.data['date'], '%Y-%m-%d')
    date = date_f.strftime(' %d %B %Y ')

    App(converter)
    mainloop()
