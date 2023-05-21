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
    plt.title(f'Топ {n} по проданным копиям')
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
