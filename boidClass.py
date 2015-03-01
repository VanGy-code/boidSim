import random
import pygame

class Boid:
	
	def __init__(self,position,size):
		
		self.position = position
		self.velocity = (random.randint(0,5000),random.randint(0,5000))
		self.radius = size/2
		
	def update(self,surface):
		pygame.draw.circle(surface, (255,255,255), self.position,self.radius, 0)

