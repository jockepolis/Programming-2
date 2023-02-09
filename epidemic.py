
import random


class Person:
    def __init__(self, is_infected, recovery_time, box_size):
        self.is_infected = is_infected
        self.recovery_time = recovery_time
        self.time_since_infection = 0
        self.box_size = box_size
        x = box_size*random.random()
        y = box_size*random.random()
        self.pos = (x, y)
    
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
            
    def main():
        # --- Simulation parameters --------------------------------
        N = 40 # Number of people
        Nsteps = 100 # Number of time steps
        box_size = 10 # Size of simulation area
        max_step = 1 # Longest possible step
        initial_infection_prob = 0.5 # Initial infection probability
        recovery_time = 10 # Time to recover after infection
        infection_radius = 0.5 # Infected individual can only infect
        # others if they are within this distance
        #-----------------------------------------------------------
        #--- Create list of Person objects ----------------------
        persons = []
        for _ in range(N):
            is_infected = random.random() < initial_infection_prob
            p = Person(is_infected, recovery_time, box_size)
            persons.append(p)
        for _ in range(Nsteps):
            for p in persons:
                p.advance_time()
            for p in persons:
                p.step(max_step)
            for i in range(N):
                for j in range(i+1, N):
                    if persons[i].distance(persons[j]) < infection_radius:
                        persons[i].handle_proximity(persons[j])
                        
if __name__== "__main__":
    main()