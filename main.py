from crud.crud_cat import Category
from crud.crud_prod import Product
from crud.reuh import display_allproducts
from graphics.window import StoreWindow
from tkinter import *

main_window = Tk()

custom_display = Label(main_window, text="Application inventaire", font=("Helvetica, 18"))

custom_display.pack()

rows = display_allproducts()
for r in rows :
    ligne = custom_display = Label(main_window, text=r, font=("Helvetica, 12"))
    ligne.pack()

main_window.mainloop()