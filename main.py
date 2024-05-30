import tkinter as tk
from tkinter import messagebox
import random

class PizzeriaGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Мини-пиццерия")
        self.geometry("800x600")
        self.iconbitmap("pizza.ico")

        # Ингредиенты и заказ клиента
        self.ingredients = ["Добавить сыр", "Добавить колбаски", "Добавить грибы", "Добавить курицу",
                            "Добавить пепперони"]
        self.sous = 'Добавить соус'
        self.client_order = []
        self.canvas = tk.Canvas(self, width=800, height=250)
        self.generate_client_order()
        self.selected_ingredients = []
        self.size = 0
        self.pech = None
        # Создание кнопок
        self.create_widgets()
        self.pizzaf = self.otris_pizza()

    def create_widgets(self):
        tk.Label(self, text="Пиццерия", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=3, pady=10)
        self.order_label = tk.Label(self, text="Заказ: " + ", ".join(self.client_order))
        self.order_label.grid(row=1, column=0, columnspan=3, pady=5)
        self.canvas.grid(row=2, column=0, columnspan=3, pady=10)

        row_idx = 3
        col_idx = 0
        for ingredient in self.ingredients:
            tk.Button(self, text=ingredient, command=lambda i=ingredient: self.add_ingredient(i)).grid(row=row_idx,
                                                                                                       column=col_idx,
                                                                                                       padx=5, pady=2)
            col_idx += 1
            if col_idx > 2:  # размещаем по 3 кнопки в ряд
                col_idx = 0
                row_idx += 1

        tk.Button(self, text=self.sous, command=lambda i=self.sous: self.add_sous(i)).grid(row=row_idx,
                                                                                           column=col_idx, padx=5,
                                                                                           pady=2)
        row_idx += 1

        self.selected_label = tk.Label(self, text="Выбранные: " + ", ".join(self.selected_ingredients))
        self.selected_label.grid(row=row_idx+1, column=0, columnspan=3, pady=10)

    def add_sous(self, sou):
        if not self.pech:
            self.pech = tk.Button(self, text="В печь", command=self.check_order)
            self.pech.grid(row=8, column=1, padx=5, pady=5)

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
        def move_pizza():
            self.canvas.move(self.pizzaf, 5, 0)
            x1, y1, x2, y2 = self.canvas.coords(self.pizzaf)
            if x1 < 800:
                self.after(50, move_pizza)
            else:
                messagebox.showinfo("Результат", "Заказ выполнен верно!")
                self.after(0, self.reset_game)  # Ensure the reset happens after the message box

        move_pizza()

    def reset_game(self):
        self.selected_ingredients = []
        self.generate_client_order()
        self.update_selected_label()
        self.order_label.config(text="Заказ: " + ", ".join(self.client_order))
        if self.pech:
            self.pech.destroy()
            self.pech = None
        self.pizzaf = self.otris_pizza()  # Create a new random-sized pizza

    def generate_client_order(self):
        self.client_order = []
        for i in range(random.randint(1, 5)):
            a = random.choice(self.ingredients)
            if a not in self.client_order:
                self.client_order.append(a)
        self.client_order.append(self.sous)

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
