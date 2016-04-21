import tkinter as tk
import pygame as pg
import math as m
import os

# Global variables
width, height, center = 640, 360, (320, 180)

line1pt1 = (-100, 100, -100)
line1pt2 = (100, 100, -100)

line2pt1 = (100, 100, -100)
line2pt2 = (100, 100, 100)

line3pt1 = (100, 100, 100)
line3pt2 = (-100, 100, 100)

line4pt1 = (-100, 100, 100)
line4pt2 = (-100, 100, -100)

line5pt1 = (-100, -100, -100)
line5pt2 = (100, -100, -100)

line6pt1 = (100, -100, -100)
line6pt2 = (100, -100, 100)

line7pt1 = (100, -100, 100)
line7pt2 = (-100, -100, 100)

line8pt1 = (-100, -100, 100)
line8pt2 = (-100, -100, -100)

line9pt1 = (-100, 100, -100)
line9pt2 = (-100, -100, -100)

line10pt1 = (100, 100, -100)
line10pt2 = (100, -100, -100)

line11pt1 = (100, 100, 100)
line11pt2 = (100, -100, 100)

line12pt1 = (-100, 100, 100)
line12pt2 = (-100, -100, 100)

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
    			v = data[1], data[2], data[3]
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
obj = OBJ('usethis.obj')
obj.read_file()

# For loop that iterates through verticies
for point in obj.read_verticies():
	print(point)

# For loop that iterates through faces
for point in obj.read_faces():
	print(point)

# Main animation loop
while 1:

	# Update  screen background
	screen.fill((0, 0, 0))

	# Set slider input
	thetay = m.radians(sliderx.get())
	thetax = m.radians(slidery.get())
	thetaz = m.radians(sliderz.get())

	# Rotate points on x, y and z axis
	newline1pt1 = rotate_point_xyz(line1pt1[0], line1pt1[1], line1pt1[2], thetax, thetay, thetaz)
	newline2pt1 = rotate_point_xyz(line2pt1[0], line2pt1[1], line2pt1[2], thetax, thetay, thetaz)
	newline3pt1 = rotate_point_xyz(line3pt1[0], line3pt1[1], line3pt1[2], thetax, thetay, thetaz)
	newline4pt1 = rotate_point_xyz(line4pt1[0], line4pt1[1], line4pt1[2], thetax, thetay, thetaz)
	newline5pt1 = rotate_point_xyz(line5pt1[0], line5pt1[1], line5pt1[2], thetax, thetay, thetaz)
	newline6pt1 = rotate_point_xyz(line6pt1[0], line6pt1[1], line6pt1[2], thetax, thetay, thetaz)
	newline7pt1 = rotate_point_xyz(line7pt1[0], line7pt1[1], line7pt1[2], thetax, thetay, thetaz)
	newline8pt1 = rotate_point_xyz(line8pt1[0], line8pt1[1], line8pt1[2], thetax, thetay, thetaz)
	newline9pt1 = rotate_point_xyz(line9pt1[0], line9pt1[1], line9pt1[2], thetax, thetay, thetaz)
	newline10pt1 = rotate_point_xyz(line10pt1[0], line10pt1[1], line10pt1[2], thetax, thetay, thetaz)
	newline11pt1 = rotate_point_xyz(line11pt1[0], line11pt1[1], line11pt1[2], thetax, thetay, thetaz)
	newline12pt1 = rotate_point_xyz(line12pt1[0], line12pt1[1], line12pt1[2], thetax, thetay, thetaz)

	newline1pt2 = rotate_point_xyz(line1pt2[0], line1pt2[1], line1pt2[2], thetax, thetay, thetaz)
	newline2pt2 = rotate_point_xyz(line2pt2[0], line2pt2[1], line2pt2[2], thetax, thetay, thetaz)
	newline3pt2 = rotate_point_xyz(line3pt2[0], line3pt2[1], line3pt2[2], thetax, thetay, thetaz)
	newline4pt2 = rotate_point_xyz(line4pt2[0], line4pt2[1], line4pt2[2], thetax, thetay, thetaz)
	newline5pt2 = rotate_point_xyz(line5pt2[0], line5pt2[1], line5pt2[2], thetax, thetay, thetaz)
	newline6pt2 = rotate_point_xyz(line6pt2[0], line6pt2[1], line6pt2[2], thetax, thetay, thetaz)
	newline7pt2 = rotate_point_xyz(line7pt2[0], line7pt2[1], line7pt2[2], thetax, thetay, thetaz)
	newline8pt2 = rotate_point_xyz(line8pt2[0], line8pt2[1], line8pt2[2], thetax, thetay, thetaz)
	newline9pt2 = rotate_point_xyz(line9pt2[0], line9pt2[1], line9pt2[2], thetax, thetay, thetaz)
	newline10pt2 = rotate_point_xyz(line10pt2[0], line10pt2[1], line10pt2[2], thetax, thetay, thetaz)
	newline11pt2 = rotate_point_xyz(line11pt2[0], line11pt2[1], line11pt2[2], thetax, thetay, thetaz)
	newline12pt2 = rotate_point_xyz(line12pt2[0], line12pt2[1], line12pt2[2], thetax, thetay, thetaz)

	# Draw lines
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline1pt1[0], center[1]+newline1pt1[1]), (center[0]+newline1pt2[0], center[1]+newline1pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline2pt1[0], center[1]+newline2pt1[1]), (center[0]+newline2pt2[0], center[1]+newline2pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline3pt1[0], center[1]+newline3pt1[1]), (center[0]+newline3pt2[0], center[1]+newline3pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline4pt1[0], center[1]+newline4pt1[1]), (center[0]+newline4pt2[0], center[1]+newline4pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline5pt1[0], center[1]+newline5pt1[1]), (center[0]+newline5pt2[0], center[1]+newline5pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline6pt1[0], center[1]+newline6pt1[1]), (center[0]+newline6pt2[0], center[1]+newline6pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline7pt1[0], center[1]+newline7pt1[1]), (center[0]+newline7pt2[0], center[1]+newline7pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline8pt1[0], center[1]+newline8pt1[1]), (center[0]+newline8pt2[0], center[1]+newline8pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline9pt1[0], center[1]+newline9pt1[1]), (center[0]+newline9pt2[0], center[1]+newline9pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline10pt1[0], center[1]+newline10pt1[1]), (center[0]+newline10pt2[0], center[1]+newline10pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline11pt1[0], center[1]+newline11pt1[1]), (center[0]+newline11pt2[0], center[1]+newline11pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newline12pt1[0], center[1]+newline12pt1[1]), (center[0]+newline12pt2[0], center[1]+newline12pt2[1]), 5)

	# Update pygame display
	pg.display.flip()

    # Update the Tk display
	root.update()