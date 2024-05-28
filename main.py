import math
import random
import time
import tkinter as tk

root = tk.Tk()
root.geometry("750x600")
root.title("Мини-пиццерия")
root.iconbitmap("pizza.ico")
root.wm_resizable(False, False)

WIDTH = 510
HEIGHT = 510
CC = WIDTH // 2, HEIGHT // 2

canvas = tk.Canvas(root, width=510, height=510)
canvas.place(x=150, y=0)
f = None

sizes = ["small", "medium", "big"]


class Base:
    def __init__(self, canvas, type):
        self.canvas = canvas
        self.id = None
        self.type = type
        self.size = 0
        self.pos = []
        self.sauce = False
        self.fill = {
            "pepp": 0,
            "chicken": 0,
            "cheese": 0,
            "mush": 0,
            "meat": 0
        }
        self.obj = []
        self.speed = 0
        self.set()


    def set(self):
        if self.type == "small":
            self.size = 300
        elif self.type == "medium":
            self.size = 400
        else:
            self.size = 500

        self.pos = [CC[0] - self.size / 2, CC[1] - self.size / 2,
                    CC[0] + self.size / 2, CC[1] + self.size / 2]
        self.id = self.canvas.create_oval(self.pos, fill="#f5deb3")
        self.obj.append(self.id)

    def draw(self):
        global order
        if canvas.coords(self.id)[0] <= 600:
            for id in self.obj:
                self.canvas.move(id, self.speed, 0)

        else:
            canvas.delete(self.id)
            for id in self.obj:
                canvas.delete(id)
            canvas.delete(order)
            size = random.choice(sizes)
            order = canvas.create_text(90, 20, text=f"Новая пицца: {size}")
            self.__init__(canvas, size)


size = random.choice(sizes)
order = canvas.create_text(90, 20, text=f"Новая пицца: {size}")
pizza = Base(canvas, size)


def add_sauce():
    pos = [CC[0] - (pizza.size - 50) / 2, CC[1] - (pizza.size - 50) / 2,
           CC[0] + (pizza.size - 50) / 2, CC[1] + (pizza.size - 50) / 2]
    pizza.obj.append(canvas.create_oval(pos, fill="tomato"))
    pizza.sauce = True
    ready()


def add_pepp():
    pos = [CC[0] - (pizza.size - 50) / 2 - 100, CC[1] - (pizza.size - 50) / 2 - 100,
           CC[0] + (pizza.size - 50) / 2 - 100, CC[1] + (pizza.size - 50) / 2 - 100]
    size = 30

    for n in range(3):
        spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
        distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)
        while distance > (pos[2] - pos[0]) / 2.5:
            spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
            distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)

        pizza.obj.append(canvas.create_oval(spawn[0], spawn[1], spawn[0] + size, spawn[1] + size, fill="red"))
        pizza.fill["pepp"] += 3


def add_chicken():
    pos = [CC[0] - (pizza.size - 50) / 2 - 100, CC[1] - (pizza.size - 50) / 2 - 100,
           CC[0] + (pizza.size - 50) / 2 - 100, CC[1] + (pizza.size - 50) / 2 - 100]
    size = 30

    for n in range(3):
        spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
        distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)
        while distance > (pos[2] - pos[0]) / 2.5:
            spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
            distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)

        pizza.obj.append(canvas.create_rectangle(spawn[0], spawn[1], spawn[0] + size, spawn[1] + size, fill="beige"))
        pizza.fill["chicken"] += 3


def add_cheese():
    pos = [CC[0] - (pizza.size - 50) / 2 - 100, CC[1] - (pizza.size - 50) / 2 - 100,
           CC[0] + (pizza.size - 50) / 2 - 100, CC[1] + (pizza.size - 50) / 2 - 100]
    size = 50

    for n in range(3):
        spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
        distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)
        while distance > (pos[2] - pos[0]) / 2.5:
            spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
            distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)

        pizza.obj.append(canvas.create_polygon(spawn[0], spawn[1],
                                               spawn[0] + size, spawn[1],
                                               spawn[0] + size / 2, spawn[1] + size, fill="gold"))
        pizza.fill["cheese"] += 3


def add_mush():
    pos = [CC[0] - (pizza.size - 50) / 2 - 100, CC[1] - (pizza.size - 50) / 2 - 100,
           CC[0] + (pizza.size - 50) / 2 - 100, CC[1] + (pizza.size - 50) / 2 - 100]
    size = 30

    for n in range(3):
        spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
        distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)
        while distance > (pos[2] - pos[0]) / 2.5:
            spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
            distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)

        pizza.obj.append(
            canvas.create_oval(spawn[0], spawn[1], spawn[0] + size, spawn[1] + size / 2, fill="darkorange4"))
        pizza.obj.append(canvas.create_rectangle(spawn[0] + size / 3, spawn[1] + size / 2,
                                                 spawn[0] + 2 * size / 3, spawn[1] + size, fill="darkorange4"))

        pizza.fill["mush"] += 3


def add_meat():
    pos = [CC[0] - (pizza.size - 50) / 2 - 100, CC[1] - (pizza.size - 50) / 2 - 100,
           CC[0] + (pizza.size - 50) / 2 - 100, CC[1] + (pizza.size - 50) / 2 - 100]
    size = 15

    for n in range(3):
        spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
        distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)
        while distance > (pos[2] - pos[0]) / 2.5:
            spawn = random.randint(pos[0], pos[2]), random.randint(pos[1], pos[3])
            distance = math.sqrt((spawn[0] - CC[0]) ** 2 + (spawn[1] - CC[1]) ** 2)

        pizza.obj.append(canvas.create_oval(spawn[0], spawn[1], spawn[0] + size, spawn[1] + size, fill="orangered2"))
        pizza.fill["meat"] += 3


def ready():
    global f
    f = tk.Button(text="В печь!", command=finish)
    f.place(x=620, y=500)


sauce = tk.Button(text="Добавить соус", command=add_sauce)
sauce.place(x=10, y=550)

pepp = tk.Button(text="Добавить пепперони", command=add_pepp)
pepp.place(x=115, y=550)

chicken = tk.Button(text="Добавить курицы", command=add_chicken)
chicken.place(x=255, y=550)

cheese = tk.Button(text="Добавить сыр", command=add_cheese)
cheese.place(x=380, y=550)

mush = tk.Button(text="Добавить грибы", command=add_mush)
mush.place(x=485, y=550)

meat = tk.Button(text="Добавить колбаски", command=add_meat)
meat.place(x=600, y=550)


def money():
    bank = 0
    for item in pizza.fill:
        bank += pizza.fill[item]
    if pizza.type == "small":
        bank += 100
    elif pizza.type == "medium":
        bank += 150
    else:
        bank += 200
    return bank


def finish():
    global f
    pizza.speed = 2
    f.destroy()
    pizza.obj.append(canvas.create_text(CC[0], CC[1], text=f"Цена пиццы: {money()} рублей."))


while True:
    root.update_idletasks()
    root.update()
    pizza.draw()
    time.sleep(0.01)