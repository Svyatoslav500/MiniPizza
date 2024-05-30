import tkinter as tk
from tkinter import messagebox
import random
import time

class PizzeriaGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Мини-пиццерия")
        self.geometry("800x600")
        self.iconbitmap("f_8326644e22ee02f9.ico")

        self.ingredients = ["Добавить сыр", "Добавить колбаски", "Добавить грибы", "Добавить курицу",
                            "Добавить пепперони"]
        self.sous = ['Добавить соус']
        self.client_order = []
        self.canvas = tk.Canvas(self, width=800, height=250)
        for i in range(random.randint(1, 5)):
            a = random.choice(self.ingredients)
            if a not in self.client_order:
                self.client_order.append(a)
            else:
                i -= 1
        self.client_order.append(self.sous[0])
        self.selected_ingredients = []
        self.size = 0
        self.pech_button = None  # Сохранение ссылки на кнопку "В печь"
        self.create_widgets()
        self.pizzaf = self.otris_pizza()

    def create_widgets(self):
        tk.Label(self, text="Пиццерия", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=3, pady=10)
        tk.Label(self, text="Заказ: " + ", ".join(self.client_order)).grid(row=1, column=0, columnspan=3, pady=5)
        self.canvas.grid(row=2, column=0, columnspan=3, pady=10)

        row_idx = 3
        col_idx = 0
        for ingredient in self.ingredients:
            tk.Button(self, text=ingredient, command=lambda i=ingredient: self.add_ingredient(i)).grid(row=row_idx,
                                                                                                       column=col_idx,
                                                                                                       padx=5, pady=2)
            col_idx += 1
            if col_idx > 2:
                col_idx = 0
                row_idx += 1

        tk.Button(self, text=self.sous[0], command=lambda i=self.sous[0]: self.add_sous(i)).grid(row=row_idx,
                                                                                                 column=col_idx, padx=5,
                                                                                                 pady=2)
        row_idx += 1

        self.selected_label = tk.Label(self, text="Выбранные: " + ", ".join(self.selected_ingredients))
        self.selected_label.grid(row=row_idx+1, column=0, columnspan=3, pady=10)

    def add_sous(self, sou):
        if not self.pech_button:  # Создаем кнопку "В печь" только один раз
            self.pech_button = tk.Button(self, text="В печь", command=self.check_order)
            self.pech_button.grid(row=8, column=1, padx=5, pady=5)

        if sou not in self.selected_ingredients:
            self.selected_ingredients.append(sou)
            self.update_selected_label()

    def add_ingredient(self, ingredient):
        if ingredient not in self.selected_ingredients:
            self.selected_ingredients.append(ingredient)
            self.update_selected_label()

    def update_selected_label(self):
        self.selected_label.config(text="Выбранные: " + ", ".join(self.selected_ingredients))

    def check_order(self):
        if sorted(self.selected_ingredients) == sorted(self.client_order):
            self.animate_pizza()
        else:
            messagebox.showwarning("Результат", "Заказ выполнен неверно!")
            self.reset_game()

    def animate_pizza(self):
        # Анимация пиццы с использованием метода after
        def move_pizza():
            self.canvas.move(self.pizzaf, 2, 0)
            x1, y1, x2, y2 = self.canvas.coords(self.pizzaf)
            if x1 >= 800:
                messagebox.showinfo("Результат", "Заказ выполнен верно!")
                self.reset_game()
            else:
                self.after(50, move_pizza)  # Повторяем перемещение через 50 мс

        move_pizza()

    def reset_game(self):
        self.selected_ingredients = []
        self.client_order = []
        for i in range(random.randint(1, 5)):
            a = random.choice(self.ingredients)
            if a not in self.client_order:
                self.client_order.append(a)
            else:
                i -= 1
        self.client_order.append(self.sous[0])
        self.update_selected_label()
        if self.pech_button:  # Уничтожаем кнопку "В печь", если она была создана
            self.pech_button.destroy()
            self.pech_button = None
        self.pizzaf = self.otris_pizza()  # Перерисовываем пиццу

    def otris_pizza(self):
        p = random.randint(0, 2)
        if p == 0:
            self.size = 50
        elif p == 1:
            self.size = 100
        elif p == 2:
            self.size = 150
        pizza = self.canvas.create_oval(350, 50, 350 + self.size, 50 + self.size, fill="yellow")
        return pizza


if __name__ == "__main__":
    game = PizzeriaGame()
    game.mainloop()
