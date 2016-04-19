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

# Define rotation functions
def rotate_point_yaxis(xcoord, ycoord, zcoord, theta):
	return (xcoord*m.cos(theta)+zcoord*m.sin(theta), ycoord, -1*xcoord*m.sin(theta)+zcoord*m.cos(theta))
	
def rotate_point_xaxis(xcoord, ycoord, zcoord, theta):
	return (xcoord, ycoord*m.cos(theta)-zcoord*m.sin(theta), ycoord*m.sin(theta)+zcoord*m.cos(theta))
	
def rotate_point_zaxis(xcoord, ycoord, zcoord, theta):
	return (xcoord*m.cos(theta)-ycoord*m.sin(theta), xcoord*m.sin(theta)+ycoord*m.cos(theta), zcoord)

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

# Main animation loop
while 1:

	# Update  screen background
	screen.fill((0, 0, 0))
	
	# Set slider input
	thetay = m.radians(sliderx.get())
	thetax = m.radians(slidery.get())
	thetaz = m.radians(sliderz.get())
	
	# Y-axis rotation
	newpt1line1pt1 = rotate_point_yaxis(line1pt1[0], line1pt1[1], line1pt1[2], thetay)
	newpt1line2pt1 = rotate_point_yaxis(line2pt1[0], line2pt1[1], line2pt1[2], thetay)
	newpt1line3pt1 = rotate_point_yaxis(line3pt1[0], line3pt1[1], line3pt1[2], thetay)
	newpt1line4pt1 = rotate_point_yaxis(line4pt1[0], line4pt1[1], line4pt1[2], thetay)
	newpt1line5pt1 = rotate_point_yaxis(line5pt1[0], line5pt1[1], line5pt1[2], thetay)
	newpt1line6pt1 = rotate_point_yaxis(line6pt1[0], line6pt1[1], line6pt1[2], thetay)
	newpt1line7pt1 = rotate_point_yaxis(line7pt1[0], line7pt1[1], line7pt1[2], thetay)
	newpt1line8pt1 = rotate_point_yaxis(line8pt1[0], line8pt1[1], line8pt1[2], thetay)
	newpt1line9pt1 = rotate_point_yaxis(line9pt1[0], line9pt1[1], line9pt1[2], thetay)
	newpt1line10pt1 = rotate_point_yaxis(line10pt1[0], line10pt1[1], line10pt1[2], thetay)
	newpt1line11pt1 = rotate_point_yaxis(line11pt1[0], line11pt1[1], line11pt1[2], thetay)
	newpt1line12pt1 = rotate_point_yaxis(line12pt1[0], line12pt1[1], line12pt1[2], thetay)
	
	newpt1line1pt2 = rotate_point_yaxis(line1pt2[0], line1pt2[1], line1pt2[2], thetay)
	newpt1line2pt2 = rotate_point_yaxis(line2pt2[0], line2pt2[1], line2pt2[2], thetay)
	newpt1line3pt2 = rotate_point_yaxis(line3pt2[0], line3pt2[1], line3pt2[2], thetay)
	newpt1line4pt2 = rotate_point_yaxis(line4pt2[0], line4pt2[1], line4pt2[2], thetay)
	newpt1line5pt2 = rotate_point_yaxis(line5pt2[0], line5pt2[1], line5pt2[2], thetay)
	newpt1line6pt2 = rotate_point_yaxis(line6pt2[0], line6pt2[1], line6pt2[2], thetay)
	newpt1line7pt2 = rotate_point_yaxis(line7pt2[0], line7pt2[1], line7pt2[2], thetay)
	newpt1line8pt2 = rotate_point_yaxis(line8pt2[0], line8pt2[1], line8pt2[2], thetay)
	newpt1line9pt2 = rotate_point_yaxis(line9pt2[0], line9pt2[1], line9pt2[2], thetay)
	newpt1line10pt2 = rotate_point_yaxis(line10pt2[0], line10pt2[1], line10pt2[2], thetay)
	newpt1line11pt2 = rotate_point_yaxis(line11pt2[0], line11pt2[1], line11pt2[2], thetay)
	newpt1line12pt2 = rotate_point_yaxis(line12pt2[0], line12pt2[1], line12pt2[2], thetay)
	
	# X-axis rotation
	newpt2line1pt1 = rotate_point_xaxis(newpt1line1pt1[0], newpt1line1pt1[1], newpt1line1pt1[2], thetax)
	newpt2line2pt1 = rotate_point_xaxis(newpt1line2pt1[0], newpt1line2pt1[1], newpt1line2pt1[2], thetax)
	newpt2line3pt1 = rotate_point_xaxis(newpt1line3pt1[0], newpt1line3pt1[1], newpt1line3pt1[2], thetax)
	newpt2line4pt1 = rotate_point_xaxis(newpt1line4pt1[0], newpt1line4pt1[1], newpt1line4pt1[2], thetax)
	newpt2line5pt1 = rotate_point_xaxis(newpt1line5pt1[0], newpt1line5pt1[1], newpt1line5pt1[2], thetax)
	newpt2line6pt1 = rotate_point_xaxis(newpt1line6pt1[0], newpt1line6pt1[1], newpt1line6pt1[2], thetax)
	newpt2line7pt1 = rotate_point_xaxis(newpt1line7pt1[0], newpt1line7pt1[1], newpt1line7pt1[2], thetax)
	newpt2line8pt1 = rotate_point_xaxis(newpt1line8pt1[0], newpt1line8pt1[1], newpt1line8pt1[2], thetax)
	newpt2line9pt1 = rotate_point_xaxis(newpt1line9pt1[0], newpt1line9pt1[1], newpt1line9pt1[2], thetax)
	newpt2line10pt1 = rotate_point_xaxis(newpt1line10pt1[0], newpt1line10pt1[1], newpt1line10pt1[2], thetax)
	newpt2line11pt1 = rotate_point_xaxis(newpt1line11pt1[0], newpt1line11pt1[1], newpt1line11pt1[2], thetax)
	newpt2line12pt1 = rotate_point_xaxis(newpt1line12pt1[0], newpt1line12pt1[1], newpt1line12pt1[2], thetax)
	
	newpt2line1pt2 = rotate_point_xaxis(newpt1line1pt2[0], newpt1line1pt2[1], newpt1line1pt2[2], thetax)
	newpt2line2pt2 = rotate_point_xaxis(newpt1line2pt2[0], newpt1line2pt2[1], newpt1line2pt2[2], thetax)
	newpt2line3pt2 = rotate_point_xaxis(newpt1line3pt2[0], newpt1line3pt2[1], newpt1line3pt2[2], thetax)
	newpt2line4pt2 = rotate_point_xaxis(newpt1line4pt2[0], newpt1line4pt2[1], newpt1line4pt2[2], thetax)
	newpt2line5pt2 = rotate_point_xaxis(newpt1line5pt2[0], newpt1line5pt2[1], newpt1line5pt2[2], thetax)
	newpt2line6pt2 = rotate_point_xaxis(newpt1line6pt2[0], newpt1line6pt2[1], newpt1line6pt2[2], thetax)
	newpt2line7pt2 = rotate_point_xaxis(newpt1line7pt2[0], newpt1line7pt2[1], newpt1line7pt2[2], thetax)
	newpt2line8pt2 = rotate_point_xaxis(newpt1line8pt2[0], newpt1line8pt2[1], newpt1line8pt2[2], thetax)
	newpt2line9pt2 = rotate_point_xaxis(newpt1line9pt2[0], newpt1line9pt2[1], newpt1line9pt2[2], thetax)
	newpt2line10pt2 = rotate_point_xaxis(newpt1line10pt2[0], newpt1line10pt2[1], newpt1line10pt2[2], thetax)
	newpt2line11pt2 = rotate_point_xaxis(newpt1line11pt2[0], newpt1line11pt2[1], newpt1line11pt2[2], thetax)
	newpt2line12pt2 = rotate_point_xaxis(newpt1line12pt2[0], newpt1line12pt2[1], newpt1line12pt2[2], thetax)
	
	# Z-axis rotation
	newpt3line1pt1 = rotate_point_zaxis(newpt2line1pt1[0], newpt2line1pt1[1], newpt2line1pt1[2], thetaz)
	newpt3line2pt1 = rotate_point_zaxis(newpt2line2pt1[0], newpt2line2pt1[1], newpt2line2pt1[2], thetaz)
	newpt3line3pt1 = rotate_point_zaxis(newpt2line3pt1[0], newpt2line3pt1[1], newpt2line3pt1[2], thetaz)
	newpt3line4pt1 = rotate_point_zaxis(newpt2line4pt1[0], newpt2line4pt1[1], newpt2line4pt1[2], thetaz)
	newpt3line5pt1 = rotate_point_zaxis(newpt2line5pt1[0], newpt2line5pt1[1], newpt2line5pt1[2], thetaz)
	newpt3line6pt1 = rotate_point_zaxis(newpt2line6pt1[0], newpt2line6pt1[1], newpt2line6pt1[2], thetaz)
	newpt3line7pt1 = rotate_point_zaxis(newpt2line7pt1[0], newpt2line7pt1[1], newpt2line7pt1[2], thetaz)
	newpt3line8pt1 = rotate_point_zaxis(newpt2line8pt1[0], newpt2line8pt1[1], newpt2line8pt1[2], thetaz)
	newpt3line9pt1 = rotate_point_zaxis(newpt2line9pt1[0], newpt2line9pt1[1], newpt2line9pt1[2], thetaz)
	newpt3line10pt1 = rotate_point_zaxis(newpt2line10pt1[0], newpt2line10pt1[1], newpt2line10pt1[2], thetaz)
	newpt3line11pt1 = rotate_point_zaxis(newpt2line11pt1[0], newpt2line11pt1[1], newpt2line11pt1[2], thetaz)
	newpt3line12pt1 = rotate_point_zaxis(newpt2line12pt1[0], newpt2line12pt1[1], newpt2line12pt1[2], thetaz)
	
	newpt3line1pt2 = rotate_point_zaxis(newpt2line1pt2[0], newpt2line1pt2[1], newpt2line1pt2[2], thetaz)
	newpt3line2pt2 = rotate_point_zaxis(newpt2line2pt2[0], newpt2line2pt2[1], newpt2line2pt2[2], thetaz)
	newpt3line3pt2 = rotate_point_zaxis(newpt2line3pt2[0], newpt2line3pt2[1], newpt2line3pt2[2], thetaz)
	newpt3line4pt2 = rotate_point_zaxis(newpt2line4pt2[0], newpt2line4pt2[1], newpt2line4pt2[2], thetaz)
	newpt3line5pt2 = rotate_point_zaxis(newpt2line5pt2[0], newpt2line5pt2[1], newpt2line5pt2[2], thetaz)
	newpt3line6pt2 = rotate_point_zaxis(newpt2line6pt2[0], newpt2line6pt2[1], newpt2line6pt2[2], thetaz)
	newpt3line7pt2 = rotate_point_zaxis(newpt2line7pt2[0], newpt2line7pt2[1], newpt2line7pt2[2], thetaz)
	newpt3line8pt2 = rotate_point_zaxis(newpt2line8pt2[0], newpt2line8pt2[1], newpt2line8pt2[2], thetaz)
	newpt3line9pt2 = rotate_point_zaxis(newpt2line9pt2[0], newpt2line9pt2[1], newpt2line9pt2[2], thetaz)
	newpt3line10pt2 = rotate_point_zaxis(newpt2line10pt2[0], newpt2line10pt2[1], newpt2line10pt2[2], thetaz)
	newpt3line11pt2 = rotate_point_zaxis(newpt2line11pt2[0], newpt2line11pt2[1], newpt2line11pt2[2], thetaz)
	newpt3line12pt2 = rotate_point_zaxis(newpt2line12pt2[0], newpt2line12pt2[1], newpt2line12pt2[2], thetaz)
	
	# Draw lines
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line1pt1[0], center[1]+newpt3line1pt1[1]), (center[0]+newpt3line1pt2[0], center[1]+newpt3line1pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line2pt1[0], center[1]+newpt3line2pt1[1]), (center[0]+newpt3line2pt2[0], center[1]+newpt3line2pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line3pt1[0], center[1]+newpt3line3pt1[1]), (center[0]+newpt3line3pt2[0], center[1]+newpt3line3pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line4pt1[0], center[1]+newpt3line4pt1[1]), (center[0]+newpt3line4pt2[0], center[1]+newpt3line4pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line5pt1[0], center[1]+newpt3line5pt1[1]), (center[0]+newpt3line5pt2[0], center[1]+newpt3line5pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line6pt1[0], center[1]+newpt3line6pt1[1]), (center[0]+newpt3line6pt2[0], center[1]+newpt3line6pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line7pt1[0], center[1]+newpt3line7pt1[1]), (center[0]+newpt3line7pt2[0], center[1]+newpt3line7pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line8pt1[0], center[1]+newpt3line8pt1[1]), (center[0]+newpt3line8pt2[0], center[1]+newpt3line8pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line9pt1[0], center[1]+newpt3line9pt1[1]), (center[0]+newpt3line9pt2[0], center[1]+newpt3line9pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line10pt1[0], center[1]+newpt3line10pt1[1]), (center[0]+newpt3line10pt2[0], center[1]+newpt3line10pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line11pt1[0], center[1]+newpt3line11pt1[1]), (center[0]+newpt3line11pt2[0], center[1]+newpt3line11pt2[1]), 5)
	pg.draw.line(screen, (0, 255, 0), (center[0]+newpt3line12pt1[0], center[1]+newpt3line12pt1[1]), (center[0]+newpt3line12pt2[0], center[1]+newpt3line12pt2[1]), 5)

	# Update pygame display
	pg.display.flip()

    # Update the Tk display
	root.update()