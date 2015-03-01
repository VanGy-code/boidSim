import pygame
import sys
from boidClass import Boid
from rules import *

def main():
	numberOfBoids = 50
	width = 640
	height = 480
	surface = pygame.display.set_mode((width,height))
	clock = pygame.time.Clock()
	mDrive = False
	mousePos = (0,0)
	simulationON = True
	m1,m2,m3,m4 = 1,1,1,1
	def createBoids():
		for i in range(numberOfBoids):
			posX = random.randint(width/2-300,width/2+300)
			posY = random.randint(height/2-200,height/2+200)
			pos = (posX, posY)
			size = 8
			b = Boid(pos,size)
			boidList.append(b)
			b.update(surface)
			pygame.display.update()
		return size
		
	
			
	
	
	boidList = []
		
			
	sizeOfBoid = createBoids()
	
	while simulationON:
		clock.tick(30)
		surface.fill((0,0,0))	
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print 'Quit'
				simulationON = False
			key = pygame.key.get_pressed()
			if key[pygame.K_d]:
				mDrive = True
				mousePos = pygame.mouse.get_pos()
			if key[pygame.K_s]:
				m1,m3 = -3, -1
			if key[pygame.K_f]:
				m1, m3 = 1, 1
		
	
		for boid in boidList:
			boid.position = boidBounds(boid, boid.position,width, height)
			v1 = [x*m1 for x in com(boid, boidList)]
			v2 = [x*m2 for x in distance(boid, boidList, sizeOfBoid)]
			v3 = [x*m3 for x in relvel(boid, boidList)]
			v4 = [x*m4 for x in mouseDrive(boid,mDrive, mousePos)]
			
			boid.velocity = tuple(map(sum,zip(v1,v2,v3,v4)))
			boid.position = tuple(map(sum,zip(boid.position,boid.velocity)))
		
		
		for boid in boidList:	
			boid.update(surface)
		
			
		pygame.display.update()	
			
			
	pygame.display.quit()		
	pygame.quit()		


if __name__ == "__main__":
	main()


	
			
