import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

label = tkinter.Label(text='ELIGE TU PERSONAJE', font=('impact', 12), bg='black', fg='white')
label.grid(column=0, row=0, sticky='ensw', )

ttk.Combobox(
    state='readonly',
    values=['Juan', 'Pedro', 'Camilo', 'Santiago'],
    font=('impact', 10),
    justify='center'
).grid(column=0, row=1, sticky='ew')

ttk.Button(
    text='Comenzar'
).grid(column=0, row=2)

window.mainloop()
