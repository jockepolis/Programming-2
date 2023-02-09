import tkinter as tk
import random

class Bubble():

    def __init__(self, canvas, x, y, size, color='red'):
        self.canvas = canvas

        self.x = x
        self.y = y

        self.start_x = x
        self.start_y = y

        self.size = size
        self.color = color

        self.circle = canvas.create_oval([x, y, x+size, y+size], outline=color, fill=color)

    def move(self):
        x_vel = random.randint(-5, 5)
        y_vel = -5

        self.canvas.move(self.circle, x_vel, y_vel)
        coordinates = self.canvas.coords(self.circle)

        self.x = coordinates[0]
        self.y = coordinates[1]

        # if outside screen -> move to start position
        if self.y < -self.size:
            self.x = self.start_x
            self.y = self.start_y
            self.canvas.coords(self.circle, self.x, self.y, self.x + self.size, self.y + self.size)

def move():
    for item in bubbles:
        item.move()

    window.after(33, move)

# --- main ---

start_x = 230
start_y = 270

window = tk.Tk()
window.geometry("1000x1000")

canvas = tk.Canvas(window, height=1000, width=1000)
canvas.grid(row=0, column=0, sticky='w')

bubbles = []
for i in range(5):
    offset = random.randint(10, 20)
    b = Bubble(canvas, start_x+10, start_y-offset, 20, 'red')
    bubbles.append(b)
for i in range(5):
    offset = random.randint(0, 10)
    b = Bubble(canvas, start_x+10, start_y-offset, 20, 'green')
    bubbles.append(b)

coord = [start_x, start_y, start_x+40, start_y+40]
rect = canvas.create_rectangle(coord, outline="Blue", fill="Blue")



move()

window.mainloop ()