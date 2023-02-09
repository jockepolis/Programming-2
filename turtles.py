from codecs import namereplace_errors
import turtle
import random

INFECTION_DISTANCE = 30
PERSON_RADIUS = 8
WIDTH, HEIGHT = 500, 500
CURSOR_SIZE = 20

# class MakePopulation(turtle.Turtle):
#     population = []

#     def __init__(self):
#         super().__init__(shape='circle')

#         self.shapesize(PERSON_RADIUS / CURSOR_SIZE)
#         self.penup()
#         self.setpos(random.randint(-WIDTH/2, WIDTH/2), random.randint(-HEIGHT/2, HEIGHT/2))

#         MakePopulation.population.append(self)

class Person(turtle.Turtle):
    population = []
    
    def __init__(self, is_infected, recovery_time, box_size):
        self.is_infected = is_infected
        self.recovery_time = recovery_time
        self.time_since_infection = 0
        self.box_size = box_size
        x = box_size*random.random()
        y = box_size*random.random()
        self.pos = (x, y)
        super().__init__(shape='circle')
        self.shapesize(PERSON_RADIUS / CURSOR_SIZE)
        self.penup()
        self.setpos(random.randint(-WIDTH/2, WIDTH/2), random.randint(-HEIGHT/2, HEIGHT/2))
        Person.population.append(self)
        
        
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
            x = random.random()
        if x < 0.5:
            self.is_infected = True
        if self.is_infected and not other.is_infected:
        # Check if other was infected by self
            x = random.random()
        if x < 0.5:
            other.is_infected = True
     

def jump(t, x, y): 
    t.penup()
    t.goto(x, y)
    t.pendown()

def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)
    return t

def rectangle(t, x, y, width, height, color): # Funktionen hämtad från uppgiften
    t = make_turtle(x, y)
    t.hideturtle()
    t.speed(0)
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

def move_random(t): # Funktionen gör att paddorna rör sig slumpmässigt enligt uppgift
    t.left(random.randint(-45, 45))
    t.forward(random.randint(0, 25))
    if abs(t.xcor()) > 250 or abs(t.ycor()) > 250: # Om någon padda befinner sig utanför kvadraten, gå tillbaks mot origo
        t.setheading(t.towards(0,0))

q = turtle.Turtle() # Skapar en padda för att rita upp rektangeln
q.speed(0)
rectangle(q, -250, -250, 500, 500, 'lightblue')
q.hideturtle()

# N = 20 # Number of people
# Nsteps = 100 # Number of time steps
# max_step = 1 # Longest possible step
# initial_infection_prob = 0.5 # Initial infection probability
# recovery_time = 100 # Time to recover after infection
# infection_radius = 0.5 # Infected individual can only infect others if they are within this distance
# box_size = 500 * 500

# persons = []
# for _ in range(N):
#     is_infected = random.random() < initial_infection_prob
#     p = Person(is_infected, recovery_time, box_size)
#     persons.append(p)
#     if p.is_infected:
#         p.color('red')
#     else:
#         p.color('green')

t = turtle.Turtle() # Skapa första paddan, den svarta
t.setheading(random.randint(0, 359))
t.speed(0)
jump(t, random.randint(-250, 250), random.randint(-250, 250))

r = turtle.Turtle() # Skapar den andra paddan, den röda
r.speed(0)
r.setheading(random.randint(0, 359))
r.color('red')
jump(r, random.randint(-250, 250), random.randint(-250, 250))

k = 0
for i in range(500): # Kör move_random för paddorna 500 gånger
    move_random(t)
    move_random(r)
    if t.distance(r) < 50: # Om de är närmre varandra än 50 l.e, skriv close
        t.write('Close')
        k += 1

print('Turtles were close to each other ' + str(k) + ' times') # Samlar ihop alla 'Close' i en sträng och ger det som output
turtle.done()