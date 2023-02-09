import tkinter as tk
import random

running = True

class Person():
    
    def __init__(self, is_infected, recovery_time, canvas, x, y, size, colour):
        self.is_infected = is_infected
        self.recovery_time = recovery_time
        self.time_since_infection = 0
        self.canvas = canvas
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.pos = (x, y)
        self.size = size
        self.color = colour
        self.circle = canvas.create_oval([x, y, x+size, y+size], outline=colour, fill=colour)
          
    def move(self):
        x_vel = random.randint(-5, 5)
        y_vel = random.randint(-5, 5)

        self.canvas.move(self.circle, x_vel, y_vel)
        coordinates = self.canvas.coords(self.circle)

        self.x = coordinates[0]
        self.y = coordinates[1]

        # if outside screen -> move to start position
        if self.y < -self.size:
            self.x = self.start_x
            self.y = self.start_y
            self.canvas.coords(self.circle, self.x, self.y, self.x + self.size, self.y + self.size)
    
    def advance_time(self):
        if self.is_infected:
            self.time_since_infection += 1
        if self.time_since_infection == self.recovery_time:
            self.is_infected = False
            self.time_since_infection = 0
            
    def distance(self, other):
        dx = self.pos[0] - other.pos[0]
        dy = self.pos[1] - other.pos[1]
        return (dx**2 + dy**2)**0.5
    
    def handle_proximity(self, other):
        if other.is_infected and not self.is_infected:
        # Check if self was infected by other
            inf = random.random()
            if inf < 0.5:
                self.is_infected = True
        if self.is_infected and not other.is_infected:
        # Check if other was infected by self
            inf = random.random()
            if inf < 0.5:
                other.is_infected = True
            
def move():
    for item in persons:
        item.move()

    window.after(1000, move) # Millisekunder
    
def start():
    global running
    running = True
    
def stop():
    global running
    running = False

window = tk.Tk()
window.title("Epidemic")
window.geometry("1000x1000")
canvas = tk.Canvas(window, height=1000, width=1000)
canvas.grid(row=0, column=0, sticky='w')
start = tk.Button(window, text="Start", command=start)
stop = tk.Button(window, text="Stop", command=stop)

if running:
    N = 20 # Number of people
    Nsteps = 1000 # Number of time steps
    initial_infection_prob = 0.33 # Initial infection probability
    recovery_time = 10 # Time to recover after infection
    infection_radius = 40 # Infected individual can only infect others if they are within this distance
    size = 20

    persons = []
    for _ in range(N):
        start_x = random.randint(0, 1000)
        start_y = random.randint(0, 1000)
        is_infected = random.random() < initial_infection_prob
        if is_infected:
            colour = 'red'
        else:
            colour = 'green'
        p = Person(is_infected, recovery_time, canvas, start_x, start_y, size, colour)
        persons.append(p)
        move()
    for _ in range(Nsteps):
        for p in persons:
            p.advance_time()
        for i in range(N):
            for j in range(i+1, N):
                if persons[i].distance(persons[j]) < infection_radius:
                    persons[i].handle_proximity(persons[j])
                    if persons[i].is_infected:
                        colour = "red"
                    elif persons[j].is_infected:
                        colour = 'red'
                    else:
                        colour = 'green'



window.mainloop ()

