import tkinter as tk
from tkinter import messagebox
import random

class PizzeriaGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Мини-пиццерия")
        self.geometry("800x600")
        self.iconbitmap("f_8326644e22ee02f9.ico")


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
        self.bank=100
        self.pizza = None  # объект пиццы на canvas
        self.p=0
        # Создание кнопок
        self.banktext=self.create_widgets()
        self.pizza,self.p = self.otris_pizza()
        self.ingredients_positions = {
            "Добавить сыр": [],
            "Добавить колбаски": [],
            "Добавить грибы": [],
            "Добавить курицу": [],
            "Добавить пепперони": [],
        }


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

        banktext=tk.Label(self,text=f"Баланс:{self.bank}", ).grid(row=row_idx+2, column=0,columnspan=3, pady=10)
        return banktext


    def add_sous(self, sou):
        if not self.pech:
            self.pech = tk.Button(self, text="В печь", command=self.check_order)
            self.pech.grid(row=8, column=1, padx=5, pady=5)

        if sou not in self.selected_ingredients:
            self.selected_ingredients.append(sou)
            self.update_selected_label()
        self.canvas.itemconfig(self.pizza, fill="navajo white", outline="yellow")
        self.bank-=1
        self.canvas.itemconfig(self.banktext, text=f"Баланс:{self.bank}")

    def add_ingredient(self, ingredient):
        if ingredient not in self.selected_ingredients:
            self.selected_ingredients.append(ingredient)
            self.update_selected_label()
            self.add_ingredient_to_pizza(ingredient)  # добавление ингредиента на пиццу

    def update_selected_label(self):
        self.selected_label.config(text="Выбранные: " + ", ".join(self.selected_ingredients))

    def check_order(self):
        if sorted(self.selected_ingredients) == sorted(self.client_order):
            self.animate_pizza()
        else:
            messagebox.showwarning("Результат", "Заказ выполнен неверно!")
            self.reset_game()
        self.money()
        print(self.bank)

    def animate_pizza(self):
        def move_pizza():
            self.canvas.move(self.pizza, 5, 0)
            x1, y1, x2, y2 = self.canvas.coords(self.pizza)
            for ingredient_list in self.ingredients_positions.values():
                for ingredient in ingredient_list:
                    self.canvas.move(ingredient, 5, 0)
            if x1 < 800:
                self.after(50, move_pizza)
            else:
                messagebox.showinfo("Результат", "Заказ выполнен верно!")
                self.after(0, self.reset_game)  # Обеспечить сброс после сообщения

        move_pizza()

    def reset_game(self):
        self.selected_ingredients = []
        self.generate_client_order()
        self.update_selected_label()
        self.order_label.config(text="Заказ: " + ", ".join(self.client_order))
        if self.pech:
            self.pech.destroy()
            self.pech = None
        self.canvas.delete("all")  # Удаление всех объектов с canvas
        self.pizza = self.otris_pizza()  # Создание новой случайного размера пиццы
        self.ingredients_positions = {  # Сброс позиций ингредиентов
            "Добавить сыр": [],
            "Добавить колбаски": [],
            "Добавить грибы": [],
            "Добавить курицу": [],
            "Добавить пепперони": [],
        }

    def generate_client_order(self):
        self.client_order = []
        for i in range(random.randint(1, 5)):
            a = random.choice(self.ingredients)
            if a not in self.client_order:
                self.client_order.append(a)
        self.client_order.append(self.sous)

    def money(self):
        if self.p==0:
            self.bank+=25
            self.canvas.itemconfig(self.banktext, text=f"Баланс:{self.bank}")
        if self.p==1:
            self.bank+=40
            self.canvas.itemconfig(self.banktext, text=f"Баланс:{self.bank}")
        if self.p==2:
            self.bank+=55
            self.canvas.itemconfig(self.banktext, text=f"Баланс:{self.bank}")


    def otris_pizza(self):
        self.p = random.randint(0, 2)
        if self.p == 0:
            self.size = 50
        elif self.p == 1:
            self.size = 100
        elif self.p == 2:
            self.size = 150
        pizza = self.canvas.create_oval(350, 50, 350 + self.size, 50 + self.size, fill="yellow")
        return pizza, self.p


    def add_ingredient_to_pizza(self, ingredient):
        # Добавление ингредиентов на пиццу в виде фигур
        colors = {
            "Добавить сыр": "gold",
            "Добавить колбаски": "red",
            "Добавить грибы": "brown",
            "Добавить курицу": "pink",
            "Добавить пепперони": "orange",

        }
        # Определение координат центра пиццы
        pizza_center_x = 350 + self.size / 2
        pizza_center_y = 50 + self.size / 2
        # Добавление ингредиентов внутрь пиццы
        if ingredient == "Добавить сыр":
            x = random.randint(int(pizza_center_x - self.size / 2), int(pizza_center_x + self.size / 2))
            y = random.randint(int(pizza_center_y - self.size / 2), int(pizza_center_y + self.size / 2))
            self.ingredients_positions[ingredient].append(
                self.canvas.create_oval(x, y, x + 10, y + 10, fill=colors[ingredient])
            )
            self.bank-=2
            self.canvas.itemconfig(self.banktext, text=f"Баланс:{self.bank}")
        elif ingredient == "Добавить колбаски":
            x = random.randint(int(pizza_center_x - self.size / 2), int(pizza_center_x + self.size / 2))
            y = random.randint(int(pizza_center_y - self.size / 2), int(pizza_center_y + self.size / 2))
            self.ingredients_positions[ingredient].append(
                self.canvas.create_rectangle(x, y, x + 10, y + 10, fill=colors[ingredient])
            )
            self.bank -= 3
            self.canvas.itemconfig(self.banktext, text=f"Баланс:{self.bank}")

        elif ingredient == "Добавить грибы":
            x = random.randint(int(pizza_center_x - self.size / 2), int(pizza_center_x + self.size / 2))
            y = random.randint(int(pizza_center_y - self.size / 2), int(pizza_center_y + self.size / 2))
            self.ingredients_positions[ingredient].append(
                self.canvas.create_oval(x, y, x + 10, y + 10, fill=colors[ingredient])
            )
            self.bank-=2
            self.canvas.itemconfig(self.banktext, text=f"Баланс:{self.bank}")

        elif ingredient == "Добавить курицу":
            x = random.randint(int(pizza_center_x - self.size / 2), int(pizza_center_x + self.size / 2))
            y = random.randint(int(pizza_center_y - self.size / 2), int(pizza_center_y + self.size / 2))
            self.ingredients_positions[ingredient].append(
                self.canvas.create_rectangle(x, y, x + 10, y + 10, fill=colors[ingredient])
            )
            self.bank-=4
            self.banktext.config(text=f"Баланс:{self.bank}")
            self.banktext.update_idletasks()

        elif ingredient == "Добавить пепперони":
            x = random.randint(int(pizza_center_x - self.size / 2), int(pizza_center_x + self.size / 2))
            y = random.randint(int(pizza_center_y - self.size / 2), int(pizza_center_y + self.size / 2))
            self.ingredients_positions[ingredient].append(
                self.canvas.create_oval(x, y, x + 15, y + 15, fill=colors[ingredient])
            )
            self.bank-=3
            self.canvas.itemconfig(self.banktext, text=f"Баланс:{self.bank}")








if __name__ == "__main__":
    game = PizzeriaGame()
    game.mainloop()
