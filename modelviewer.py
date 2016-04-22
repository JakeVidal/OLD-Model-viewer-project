import tkinter as tk
import pygame as pg
import math as m
import os

# Global variables
width, height, center = 640, 360, (320, 180)

# OBJ class definition from reading file
class OBJ:
    def __init__(self, fname):
        self.verticies = []
        self.faces = []
        self.filename = fname

    def read_file(self):
    	for line in open(self.filename, 'r'):
    		if line.startswith('#'): continue
    		data = line.split()
    		if data[0] == 'v':
    			v = [data[1], data[2], data[3]]
    			self.verticies.append(v)
    		if data[0] == 'f':
    			f = []
    			data.pop(0)
    			for point in data:
    				f.append(point)
    			self.faces.append(f)

    def read_verticies(self):
    	return self.verticies

    def read_faces(self):
    	return self.faces

# Define rotation functions
def rotate_point_yaxis(xcoord, ycoord, zcoord, theta):
	return (xcoord*m.cos(theta)+zcoord*m.sin(theta), ycoord, -1*xcoord*m.sin(theta)+zcoord*m.cos(theta))
	
def rotate_point_xaxis(xcoord, ycoord, zcoord, theta):
	return (xcoord, ycoord*m.cos(theta)-zcoord*m.sin(theta), ycoord*m.sin(theta)+zcoord*m.cos(theta))
	
def rotate_point_zaxis(xcoord, ycoord, zcoord, theta):
	return (xcoord*m.cos(theta)-ycoord*m.sin(theta), xcoord*m.sin(theta)+ycoord*m.cos(theta), zcoord)

def rotate_point_xyz(xcoord, ycoord, zcoord, thetax, thetay, thetaz):
	a = rotate_point_xaxis(xcoord, ycoord, zcoord, thetax)
	b = rotate_point_yaxis(a[0], a[1], a[2], thetay)
	return rotate_point_zaxis(b[0], b[1], b[2], thetaz)

# Add tkinter widgets placing pygame in embed
root = tk.Tk()
root.title("Model Viewer")
root.iconbitmap('icon.ico')
embed = tk.Frame(root, width=width, height=height)
embed.pack()
sliderz = tk.Scale(root, from_=-180, to=180, orient=tk.HORIZONTAL, label='Z-axis')
sliderz.pack(side=tk.RIGHT)
slidery = tk.Scale(root, from_=-180, to=180, orient=tk.HORIZONTAL, label='Y-axis')
slidery.pack(side=tk.RIGHT)
sliderx = tk.Scale(root, from_=-180, to=180, orient=tk.HORIZONTAL, label='X-axis')
sliderx.pack(side=tk.RIGHT)

# Tell pygame's SDL window which window ID to use    
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

# Show the window so it's assigned an ID.
root.update()

# Usual pygame initialization
pg.display.init()
screen = pg.display.set_mode((width,height))

# Initialize OBJ object
obj = OBJ('usethis2.obj')
obj.read_file()

# Main animation loop
while 1:

	# Update  screen background
	screen.fill((0, 0, 0))

	# Set slider input
	thetay = m.radians(sliderx.get())
	thetax = m.radians(slidery.get())
	thetaz = m.radians(sliderz.get())

	# For loop that iterates through verticies and rotates them in 3D space
	rotated_verticies = []
	for vertex in obj.read_verticies():
		rotated_verticies.append(rotate_point_xyz(float(vertex[0]), float(vertex[1]), float(vertex[2]), thetax, thetay, thetaz))

	# For loop that draws a wireframe of the object
	for face in obj.read_faces():
		i = 0
		while i < len(face) - 1:
			pg.draw.line(screen, (0, 255, 0), (center[0]+rotated_verticies[int(face[i])-1][0], center[1]+rotated_verticies[int(face[i])-1][1]), (center[0]+rotated_verticies[int(face[i+1])-1][0], center[1]+rotated_verticies[int(face[i+1])-1][1]), 1)
			i = i + 1
		pg.draw.line(screen, (0, 255, 0), (center[0]+rotated_verticies[int(face[i])-1][0], center[1]+rotated_verticies[int(face[i])-1][1]), (center[0]+rotated_verticies[int(face[0])-1][0], center[1]+rotated_verticies[int(face[0])-1][1]), 1)

	# Update pygame display
	pg.display.flip()

    # Update the Tk display
	root.update()