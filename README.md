<p align = "center">МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ
РОССИЙСКОЙ ФЕДЕРАЦИИ
ФЕДЕРАЛЬНОЕ ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ
ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ ВЫСШЕГО ОБРАЗОВАНИЯ
«САХАЛИНСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»</p>
<br>
<p align = "center">Институт естественных наук и техносферной безопасности</p>
<p align = "center">Кафедра информатики</p>
<p align = "center">Пак Никита Витальевич</p>
<br>
<p align = "center">Лабораторная работа</p>
<p align = "center">01.03.02 Прикладная математика и информатика</p>
<br><br><br><br><br><br><br><br>
<p align = "center" >Южно-Сахалинск</p>
<p align = "center" >2023 г.</p>

***

<p align = "center" ><b>ВВЕДЕНИЕ</b></p>
<p>Python (в русском языке встречаются названия пито́н или па́йтон) — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью языка является выделение блоков кода пробельными отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++</p>
<p>Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, объектно-ориентированное программирование, метапрограммирование и функциональное программирование. Задачи обобщённого программирования решаются за счёт динамической типизации. Аспектно-ориентированное программирование частично поддерживается через декораторы, более полноценная поддержка обеспечивается дополнительными фреймворками. Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений. Основные архитектурные черты — динамическая типизация, автоматическое управление памятью, полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора, высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты</p>
<p align = "center" >РЕШЕНИЕ ЗАДАЧ</p>

<p align = "center" >Найти любой источник данных в интернете, загрузить с помощью pandas, посчитать основные статистики, построить произвольные графики в matplotlib.</p>

```python
      
import pandas as pd
import tkinter as tk
from tkinter import ttk
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

chocolate = pd.read_excel('Top10ChocolateBars.xlsx')

root = tk.Tk()
root.title("Статистика")
root.geometry("1500x800")
root.minsize(1000, 500)
cols = ("Brand","Rank","Year","Manufacturer","Country","popularity")
table = ttk.Treeview(root, columns=cols, show="headings")
table.configure(height=25)

table.heading("Brand", text="Марка")
table.heading("Rank", text="Ранг")
table.heading("Year", text="Год")
table.heading("Manufacturer", text="Производитель")
table.heading("Country", text="Страна")
table.heading("popularity", text="Популярность")

table.column("Brand", width=150, stretch=True)
table.column("Rank", width=100, stretch=True)
table.column("Year", width=100, stretch=True)
table.column("Manufacturer", width=200, stretch=True)
table.column("Country", width=100, stretch=True)
table.column("popularity", width=100, stretch=True)


for i in range(0, len(chocolate)):
    Brand = chocolate.loc[i, 'Brand']
    Rank = chocolate.loc[i, 'Rank']
    Year = chocolate.loc[i, 'Year']
    Manufacturer = chocolate.loc[i, 'Manufacturer']
    Country = chocolate.loc[i, 'Country']
    popularity = chocolate.loc[i, 'popularity']

    table.insert(parent='', index='end', values=(Brand,Rank,Year,Manufacturer,Country,popularity))

def statistic():
    result_text = "По производителям шоколадных батончиков"
    length = len(chocolate['Manufacturer'].tolist())
    exp_level = Counter(chocolate['Manufacturer'].tolist())
    for item, value in exp_level.items():
        result = round(value / length * 100)
        result_text += "\n" + str(item) + ": " + str(result) + "%"
    label = tk.Label(root, text=result_text, font=12);
    label.pack(side=tk.LEFT)

    result_text = "По странам:"
    length = len(chocolate['Country'].tolist())
    exp_level = Counter(chocolate['Country'].tolist())
    for item, value in exp_level.items():
        result = round(value / length * 100)
        result_text += "\n" + str(item) + ": " + str(result) + "%"
    label = tk.Label(root, text=result_text, font=12);
    label.pack(side=tk.LEFT)

    result_text = "Первое место среди других шоколадных батончиков "
    first = max(chocolate['popularity'].tolist())
    second = chocolate['Brand'].tolist()
    result_text += '\n' + str(second[0]) + "= " + str(first) + "%"
    label = tk.Label(root, text=result_text, font=12);
    label.pack(side=tk.LEFT)

def Plot():
    fig, ax = plt.subplots(figsize=(5, 5))
    data = Counter(chocolate["Manufacturer"])
    x = data.keys()
    y = data.values()
    ax.pie(y, labels=x, autopct=make_autopct(y), shadow=True, startangle=180)
    plt.title('Лидеры среди производителей')
    plt.show()

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.yaxis.set_major_formatter(persent)
    n = 5
    data = chocolate["popularity"][:n]
    x = []
    for i in range(0, n):
        x.append(chocolate["Brand"][i])
    y = data
    ax.bar(x, y)
    plt.title(f'Топ {n} брендов')
    plt.ylim((min(y-4), max(y+20)))
    plt.show()

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

def persent(x, pos):
    return f'{int(x)} %'

table.pack()
statistic()
Plot()
root.mainloop()

```

***

![Screenshot](https://github.com/Pupkapus/python_lab/blob/main/Screenshot_1.png)
![Screenshot](https://github.com/Pupkapus/python_lab/blob/main/Screenshot_2.png)
![Screenshot](https://github.com/Pupkapus/python_lab/blob/main/Screenshot_3.png)

***
