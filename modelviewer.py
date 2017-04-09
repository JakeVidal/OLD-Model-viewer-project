import Tkinter as tk
import pygame as pg
import math as m
import random as r
from operator import add
import os

# Global variables
width, height, center = 1280, 720, (640, 360)
first_iteration = True

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

def scale_point(xcoord, ycoord, zcoord, factor):
    return (float(factor*xcoord/100), float(factor*ycoord/100), float(factor*zcoord/100))

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
sliderf = tk.Scale(root, from_=1, to=500, orient=tk.HORIZONTAL, label='Scale factor')
sliderf.pack(side=tk.RIGHT)

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
    screen.fill((100, 100, 100))

    # Set slider input
    thetay = m.radians(sliderx.get())
    thetax = m.radians(slidery.get())
    thetaz = m.radians(sliderz.get())
    factor = sliderf.get()

    #For loop that scales the object to the correct size
    scaled_verticies = []
    for vertex in obj.read_verticies():
        scaled_verticies.append(scale_point(float(vertex[0]), float(vertex[1]), float(vertex[2]), factor))

    # For loop that iterates through verticies and rotates them in 3D space
    rotated_verticies = []
    for vertex in scaled_verticies:
        rotated_verticies.append(rotate_point_xyz(float(vertex[0]), float(vertex[1]), float(vertex[2]), thetax, thetay, thetaz))

    # For loop that chooses the correct order to draw the faces of the object to prevent overlap
    i = 0
    draw_order = []
    face_list = obj.read_faces()
    for face in face_list:
        min_z_value = 1000000000
        for vertex in face:
            if rotated_verticies[int(vertex)-1][2] < min_z_value: min_z_value = rotated_verticies[int(vertex)-1][2]
        draw_order.append([min_z_value, i])
        i = i + 1
    draw_order.sort()

    # Generate the color of the object
    if first_iteration:
        color_list = []
        for i in range(len(face_list)):
          color_list.append((10+r.randint(0,100), 155+r.randint(0,100), 10+r.randint(0,100)))

    # For loop that draws the faces and perimeter lines of the object
    for element in draw_order:
        face = face_list[element[1]]
        point_list = []
        for vertex in face:
            point_list.append((center[0]+rotated_verticies[int(vertex)-1][0], center[1]+rotated_verticies[int(vertex)-1][1]))
        pg.draw.polygon(screen, color_list[element[1]], point_list)
        pg.draw.lines(screen, (0, 0, 0), True, point_list, 3)

    # Update pygame display
    pg.display.flip()

    # Update the Tk display
    root.update()

    first_iteration = False