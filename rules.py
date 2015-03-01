import random
import pygame


def com(boid, boidList):
	centreOfMass = (0,0)
	ourBoid = boid
	for boidl in boidList:
		if not boidl == ourBoid:
			centreOfMass = map(sum,(zip(centreOfMass,boidl.position)))

	centreOfMass[:] = [x/(len(boidList)-1)	for x in centreOfMass]
	centreOfMass[:] = [(x-y)/100 for x,y in zip(tuple(centreOfMass), ourBoid.position)]


	

	
	return tuple(centreOfMass)


def distance(boid, boidList, sizeOfBoid):
	c = (0,0)
	ourBoid = boid
	for boidl in boidList:
		if not boidl == ourBoid:
			if abs(boidl.position[0] - ourBoid.position[0]) < sizeOfBoid*1.5 and abs(boidl.position[1] - ourBoid.position[1]) < sizeOfBoid*1.5:
				dif = tuple([(x-y) for x,y in zip(boidl.position,ourBoid.position)])
				c = tuple([(x-y) for x,y in zip(c,dif)])
	return c

def relvel(boid, boidList):
	pv = (0,0)	
	ourBoid = boid	
	for boid in boidList:
		if not boid == ourBoid:
			pv = map(sum,(zip(pv, boid.velocity)))
			
	pv[:] = [x/(len(boidList)-1) for  x in pv]		
	pv[:] = [(x-y)/8 for x,y in zip(tuple(pv), ourBoid.velocity)]
	return tuple(pv)


def boidBounds(boid, position, width, height):
		Xmax = width - 10
		Ymax = height - 10
		Xmin =  10
		Ymin =  10
		posVector = [0,0]

		if position[0]< Xmin:
			posVector[0] = width
		elif position[0]> Xmax:
			posVector[0] = -width


		if position[1]< Ymin:
			posVector[1] = height

		elif position[1]> Ymax:
			posVector[1] = -height
		
		
		return tuple([x+y for x,y in zip(posVector,position)])

def mouseDrive(boid, mDrive, mousePos):
	
	if mDrive:
		driveVector = [(x-y)/100 for x,y in zip(tuple(mousePos), boid.position)]
	else:
		driveVector = (0,0)
	return tuple(driveVector)	
