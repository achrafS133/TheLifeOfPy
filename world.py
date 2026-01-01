import pygame
import random
import numpy as np
from organism import Organism
from food import Food

class World:
    def __init__(self, width, height, num_organisms=20, num_food=50):
        self.width = width
        self.height = height
        self.organisms = [Organism(random.randint(0, width), random.randint(0, height)) for _ in range(num_organisms)]
        self.foods = [Food(random.randint(0, width), random.randint(0, height)) for _ in range(num_food)]
        self.generation = 1
        self.max_food = num_food

    def update(self):
        # Update organisms
        for org in self.organisms[:]:
            org.update(self.width, self.height, self.foods)
            
            # Check if dead
            if not org.alive:
                self.organisms.remove(org)
                continue

            # Check food consumption
            for food in self.foods[:]:
                dist = np.linalg.norm(org.pos - food.pos)
                if dist < org.radius + food.radius:
                    org.energy = min(org.max_energy, org.energy + food.energy_value)
                    self.foods.remove(food)

            # Check reproduction
            if org.energy >= org.reproduction_threshold:
                child = org.reproduce()
                self.organisms.append(child)

        # Check extinction and reset
        if len(self.organisms) == 0:
            self.generation += 1
            num_to_spawn = 20
            self.organisms = [Organism(random.randint(0, self.width), random.randint(0, self.height)) for _ in range(num_to_spawn)]

        # Respawn food
        while len(self.foods) < self.max_food:
            self.foods.append(Food(random.randint(0, self.width), random.randint(0, self.height)))

    def draw(self, surface):
        for food in self.foods:
            food.draw(surface)
        for org in self.organisms:
            org.draw(surface)

    def get_stats(self):
        return {
            "Population": len(self.organisms),
            "Generation": self.generation,
            "Food Count": len(self.foods)
        }
