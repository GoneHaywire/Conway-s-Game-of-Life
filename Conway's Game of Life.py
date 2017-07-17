import random
import time as Time
import argparse
from sys import exit

legend = {1: "x", 0: " "}
count = 0
time = 0

parser = argparse.ArgumentParser()
parser.add_argument('width', type=int, help='width of the grid, 77 recommended', default=77)
parser.add_argument('height', type=int, help='height of the grid, 21 recommended', default=21)
args = parser.parse_args()

def grid_print(grid):
	line = "|"
	print "\n" * int(22-args.height)
	print "+" + "-" * (args.width) + "+"
	for num in range(1, len(grid)+1):
		line += legend[grid[num-1]]
		if num % args.width == 0:
			line += "|"
			print line
			line = "|"
	print "+" + "-" * (args.width) + "+"
	print "Time:", time, "   Population:", grid.count(1)
	if grid.count(1) == 0: exit("All cells died.")

def health_check():
	global curr_grid, neighbour_grid
	for num in range(len(curr_grid)):
		neighbours = 0

		if num == 0: #top-left corner
			if curr_grid[1]:
				neighbours += 1
			if curr_grid[args.width]:
				neighbours += 1
			if curr_grid[args.width+1]:
				neighbours += 1
				
		elif num == args.width-1: #top-right corner
			if curr_grid[num-1]:
				neighbours += 1
			if curr_grid[args.width+num]:
				neighbours += 1
			if curr_grid[args.width+(num-1)]:
				neighbours += 1
			
		elif num == args.width*args.height-args.width: #bottom-left corner
			if curr_grid[num-args.width]:
				neighbours += 1
			if curr_grid[num+1]:
				neighbours += 1
			if curr_grid[num-(args.width-1)]:
				neighbours += 1
				
		elif num == (args.width*args.height)-1: #bottom-right corner
			if curr_grid[num-1]:
				neighbours += 1
			if curr_grid[num-args.width]:
				neighbours += 1
			if curr_grid[num-(args.width+1)]:
				neighbours += 1
			
		elif num in [x for x in range(1, args.width-1)]: #top
			if curr_grid[num-1]:
				neighbours += 1
			if curr_grid[num+1]:
				neighbours += 1
			if curr_grid[num+(args.width-1)]:
				neighbours += 1
			if curr_grid[num+args.width]:
				neighbours += 1
			if curr_grid[num+args.width+1]:
				neighbours += 1
			
		elif num in [x for x in range((args.width*args.height)-(args.width-1), (args.width*args.height-1))]: #bottom
			if curr_grid[num-1]:
				neighbours += 1
			if curr_grid[num+1]:
				neighbours += 1
			if curr_grid[num-(args.width+1)]:
				neighbours += 1
			if curr_grid[num-args.width]:
				neighbours += 1
			if curr_grid[num-(args.width-1)]:
				neighbours += 1
			
		elif num in [x for x in range(args.width, (args.width*args.height)-9, args.width)]: #left
			if curr_grid[num-args.width]:
				neighbours += 1
			if curr_grid[num+args.width]:
				neighbours += 1
			if curr_grid[num-(args.width-1)]:
				neighbours += 1
			if curr_grid[num+(args.width+1)]:
				neighbours += 1
			if curr_grid[num+1]:
				neighbours += 1
			
		elif num in [x for x in range(2*args.width-1, (args.width*args.height)-args.width, args.width)]: #right
			if curr_grid[num-(args.width+1)]:
				neighbours += 1
			if curr_grid[num+args.width]:
				neighbours += 1
			if curr_grid[num-args.width]:
				neighbours += 1
			if curr_grid[num-1]:
				neighbours += 1
			if curr_grid[num+(args.width-1)]:
				neighbours += 1
			
		else: #middle
			if curr_grid[num-(args.width+1)]:
				neighbours += 1
			if curr_grid[num-args.width]:
				neighbours += 1
			if curr_grid[num-(args.width-1)]:
				neighbours += 1
			if curr_grid[num-1]:
				neighbours += 1
			if curr_grid[num+1]:
				neighbours += 1
			if curr_grid[num+(args.width-1)]:
				neighbours += 1
			if curr_grid[num+args.width]:
				neighbours += 1
			if curr_grid[num+(args.width+1)]:
				neighbours += 1
				
		neighbour_grid[num] = neighbours	

def cell_removal():
	global curr_grid
	for cell_num in range(len(curr_grid)):
		if neighbour_grid[cell_num] < 2:
			curr_grid[cell_num] = 0
		elif neighbour_grid[cell_num] > 3:
			curr_grid[cell_num] = 0
				
def cell_birth():
	global curr_grid
	for cell_num in range(len(curr_grid)):
		if neighbour_grid[cell_num] == 3:
			curr_grid[cell_num] = 1
		
curr_grid = [0 for x in range(args.width*args.height)]
neighbour_grid = [0 for x in range(args.width*args.height)]

for i in range((args.width*args.height)*15/100):
	randint = random.randint(0, args.width*args.height-1)
	curr_grid[randint] = 1
			
try:
	while 1:
		grid_print(curr_grid)
		health_check()
		cell_removal()
		cell_birth()
		time += 1
		Time.sleep(0.3)
		
except KeyboardInterrupt:
	print "Stopped."