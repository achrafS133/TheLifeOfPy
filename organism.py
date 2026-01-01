import numpy as np
import random
import pygame
import math
from neural_network import NeuralNetwork

class Organism:
    def __init__(self, x, y, radius=5, color=None, brain=None):
        self.pos = np.array([float(x), float(y)])
        # Initial velocity
        angle = random.uniform(0, 2 * math.pi)
        self.vel = np.array([math.cos(angle), math.sin(angle)])
        
        self.radius = radius
        self.color = color if color else (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.energy = 100.0
        self.max_energy = 200.0
        self.reproduction_threshold = 150.0
        self.alive = True
        self.speed_multiplier = 3.0
        
        if brain:
            self.brain = brain
        else:
            self.brain = NeuralNetwork(input_size=2, hidden_size=6, output_size=2)

    def sense(self, foods):
        if not foods:
            return np.array([0.0, 0.0]) # No food, return neutral inputs

        # Find nearest food
        nearest_food = None
        min_dist = float('inf')
        for food in foods:
            dist = np.linalg.norm(self.pos - food.pos)
            if dist < min_dist:
                min_dist = dist
                nearest_food = food
        
        if not nearest_food:
            return np.array([0.0, 0.0])

        # Input 1: Normalized Distance (0 to 1, where 1 is close, 0 is far)
        # Assuming max sensing distance is around 500
        norm_dist = 1.0 - min(min_dist / 500.0, 1.0)

        # Input 2: Angle to food relative to current velocity
        target_vec = nearest_food.pos - self.pos
        target_angle = math.atan2(target_vec[1], target_vec[0])
        current_angle = math.atan2(self.vel[1], self.vel[0])
        
        diff_angle = target_angle - current_angle
        # Normalize to [-1, 1]
        while diff_angle > math.pi: diff_angle -= 2 * math.pi
        while diff_angle < -math.pi: diff_angle += 2 * math.pi
        norm_angle = diff_angle / math.pi

        return np.array([norm_dist, norm_angle])

    def decide(self, inputs):
        outputs = self.brain.process(inputs)
        # outputs[0] is speed adjustment (-1 to 1) -> map to (0 to 1)
        # outputs[1] is rotation (-1 to 1)
        speed_factor = (outputs[0] + 1) / 2
        rotation = outputs[1] * 0.2 # Max rotation per frame
        return speed_factor, rotation

    def update(self, width, height, foods):
        # 1. Sense
        inputs = self.sense(foods)
        
        # 2. Decide
        speed_factor, rotation = self.decide(inputs)
        
        # 3. Apply Decision
        # Rotate velocity vector
        current_angle = math.atan2(self.vel[1], self.vel[0])
        new_angle = current_angle + rotation
        self.vel = np.array([math.cos(new_angle), math.sin(new_angle)])
        
        # Move
        effective_speed = self.speed_multiplier * speed_factor
        self.pos += self.vel * effective_speed

        # Boundary checks (teleport or bounce - let's bounce for now)
        if self.pos[0] < 0: self.pos[0] = 0; self.vel[0] *= -1
        if self.pos[0] > width: self.pos[0] = width; self.vel[0] *= -1
        if self.pos[1] < 0: self.pos[1] = 0; self.vel[1] *= -1
        if self.pos[1] > height: self.pos[1] = height; self.vel[1] *= -1

        # Energy consumption proportional to speed and size
        # Moving faster costs more energy
        energy_loss = 0.05 + (effective_speed * 0.02) + (self.radius * 0.005)
        self.energy -= energy_loss

        if self.energy <= 0:
            self.alive = False

    def draw(self, surface):
        if self.alive:
            # Draw body
            pygame.draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
            # Draw eye/direction indicator
            eye_pos = self.pos + self.vel * (self.radius * 0.8)
            pygame.draw.circle(surface, (255, 255, 255), (int(eye_pos[0]), int(eye_pos[1])), 2)

    def reproduce(self):
        # Split energy
        self.energy /= 2
        # Clone brain and mutate
        child_brain = self.brain.copy()
        child_brain.mutate(rate=0.2, magnitude=0.3)
        
        child = Organism(self.pos[0] + random.uniform(-10, 10), 
                        self.pos[1] + random.uniform(-10, 10), 
                        self.radius, 
                        self.color,
                        brain=child_brain)
        child.energy = self.energy
        return child
