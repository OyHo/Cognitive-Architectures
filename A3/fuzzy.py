
from sys import argv
import matplotlib.pyplot as plt

#input variables
distance_init = 3.7
delta_init =  1.2
distdelt = {}

# Defining sets
distanceset = {
    "start": 0,
    "end": 10,
    "name": {
        "VerySmall": (0, 1.25, 2.5, 1.0),
        "Small": (1.5, 3, 4.5, 1.0),
        "Perfect": (3.5, 5, 6.5, 1.0),
        "Big": (5.5, 7,  8.5, 1.0),
        "VeryBig": (7.5, 9, 10, 10)
    }
}

deltaset = {
    "start": -5,
    "end": 5,
    "name": {
        "ShringkingFast": (0, -4, -2.5, 1.0),
        "Shrinking": (-3.5, -2, -0.5, 1.0),
        "Stable": (-1.5, 0, 1.5, 1.0),
        "Growing": (0.5, 2, 3.5, 1.0),
        "GrowingFast": (2.5, 4, 5, 1.0)
    }
}

actionset = {
    "start": -10,
    "end": 10,
    "name": {
        "BrakeHard": (-10, -10, -8, -5),
        "SlowDown": (-7, -4, -4, -1),
        "None": (-3, 0, 0, 3),
        "SpeedUp": (1, 4, 4, 7),
        "FloorIt": (5, 8, 10, 10)
    }
}

sets = {"distance": distanceset, "delta": deltaset}

# Functions for finding values
def triangle(pos, x0, x1, x2, clip):
	val = 0.0
	if (pos >= x0 and pos <= x1):
		val = (pos -x0)/(x1 - x0)
	elif (pos >= x1 and pos <= x2):
		val = (x2 - pos)/(x1 - x0)
	if (val > clip):
		val = clip
	return val

def grade(pos, x0, x1, clip):
	val = 0.0
	if(pos >= x1):
		val = 1.0
	elif(pos <= x0):
		val = 0.0
	else:
		val = (pos - x0)/(x1 - x0)
	if(val > clip):
		val = clip
	return val

def reverse_grade(pos, x0, x1, clip):
	val = 0.0
	if(pos >= x1):
		val = 0.0
	elif(pos <= x0):
		val = 1.0
	else:
		val = (pos - x0)/(x1 - x0)
	if(val > clip):
		val = clip
	return val


def AND(x0,x1):
	return min(x0,x1)

def OR(x0,x1):
	return max(x0,x1)

def NOT(x):
	return 1-x


def fuzz(set): # contains both fuzzyfication logic and rules. Takes in a set and splits it
	dist = set["distance"]
	delt = set["delta"]
	distdelt = {} # make a new list of distdelt
	distdelt["None"] = AND(triangle(distance_init, 1.5, 3, 4.5, 1.0), triangle(delta_init, 0.5, 2, 3.5, 1.0))
	distdelt["SlowDown"] = AND(triangle(distance_init, 1.5, 3.0, 4.5, 1.0), triangle(delta_init,-1.5, 0, 1.5, 1.0))
	distdelt["SpeedUp"] = AND(triangle(distance_init, 3.5, 5.0, 6.5, 1.0), triangle(delta_init, 0.5, 2, 3.5, 1.0))
	distdelt["FloorIt"] = AND(grade(distance_init, 7.5, 10.0, 1.0), OR(NOT(triangle(delta_init, 0.5, 2, 3.5, 1.0)), NOT(grade(delta_init, 2.5, 4, 1.0))))
	distdelt["BrakeHard"] = reverse_grade(distance_init, 0.0, 2.5, 1.0)
	return distdelt
	
def defuzz(distdelt):
	above = (((-10 - 9 - 8 - 7 - 6 - 5) * distdelt['BrakeHard'])
			 + ((-7 - 6 - 5 - 4 - 3 - 2 - 1) * distdelt['SlowDown'])
			 + ((-3 - 2 - 1 + 0 + 1 + 2 + 3) * distdelt['None'])
			 + ((1 + 2 + 3 + 4 + 5 + 6 + 7) * distdelt['SpeedUp'])
			 + ((5 + 6 + 7 + 8 + 9 + 10) * distdelt['FloorIt']))
	below = (distdelt['BrakeHard'] * 6
			 + distdelt['SlowDown'] * 7
			 + distdelt['None'] * 7
			 + distdelt['SpeedUp'] * 7
			 + distdelt['FloorIt'] * 6)

	print (1 + above / below)


def main ():
    distdelt = fuzz(sets)
    print(distdelt)
    defuzz(distdelt)
main()