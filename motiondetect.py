# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:02:46 2023

@author: Sofiene
"""

import pygame
import numpy as np
from math import sin
import cv2
from pygame import QUIT


def Track_Motion():
    # Define the list of colors
    list_of_colors = [(78, 168, 222), (114, 239, 221), (100, 223, 223), (86, 207, 225), (72, 191, 227),
                      (74, 167, 202), (83, 144, 217), (94, 96, 206), (105, 48, 195), (116, 0, 184)]

    # Initialize Pygame
    pygame.init()

    # Initialize the display
    width, height = 1920, 1080
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Video Edge Detection")

    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Initialize the previous frame
    ret, prev_frame = cap.read()
    prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    # Create the clock for frame rate control
    clock = pygame.time.Clock()

    # Define the grid parameters
    grid_size = 17

    num_rows = height // grid_size
    num_cols = width // grid_size
    polygons = []
    # this is the polygon for drawing them
    def polygon(surface, color, x, y, radius, npoints):
        angle = 2 * np.pi / npoints
        points = []
        for i in range(npoints):
            angle_i = i * angle
            x_i = x + radius * np.cos(angle_i)
            y_i = y + radius * np.sin(angle_i)
            points.append((int(x_i), int(y_i)))
        pygame.draw.polygon(surface, color, points)
    #mapping function to deside the polgone that are colored but notice that needs the brightness to be well excuted else it will be a mess of filled screen with polgones !
    def map_range(value, from_low, from_high, to_low, to_high):
        return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low

    def map_color(x, y):
        # You can customize this function to map x and y to a specific color
        # Here, we use a simple example of mapping x to the red channel and y to the blue channel
        clr = list_of_colors[int(((sin(x * y)) * 5) - 1)]
        # Blue channel (0-255)
        return clr
    #the event loop for the pygame app !
    running = True
    while running:
        for event in pygame.event.get():
            #to quit the app !
            if event.type == QUIT:
                running = False
        #reading the video cam and storing the ret and frame vars
        ret, frame = cap.read()
        #retreving the colors of the frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #masking the frame by differtiating the frame and the previous frame to make an edge detection
        frame_diff = cv2.absdiff(frame, prev_frame)
        # _, frame_diff = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY) WE DONT NEED THIS
        frame_diff[frame_diff < 50] = 0
        prev_frame = frame

        frame_diff = cv2.resize(frame_diff, (width, height))
        frame_diff = cv2.cvtColor(frame_diff, cv2.COLOR_GRAY2BGR)
        #BACKGROUND COLOR AS U SEE
        background_color = (10, 2, 4)
        # THIS FOR THE POLGONS TO LEAVE TRAILS BEHIND THEM (the more its low the more u see trails)
        alpha_value = 30
        # Set the alpha value (transparency)

        # Create a new surface with the desired background color and alpha
        background_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        pygame.draw.rect(background_surface, background_color + (alpha_value,), (0, 0, width, height))

        # Blit the background surface onto the main screen
        screen.blit(background_surface, (0, 0))
        #this for setuping the grid by polygons to make the code more efficient we didnt actually draw a polygon in every pixel !
        for row in range(num_rows):
            for col in range(num_cols):
                x = col * grid_size
                y = row * grid_size
                color = frame_diff[y, x]  # Get the color of the pixel at this position
                brightness = sum(color) / 3  # Calculate brightness

                # Map brightness to polygon size
                size = map_range(-brightness, -255, 0, grid_size, 0)

                # Get a random color for the polygon
                # color = list_of_colors[int(np.random.randint(len(list_of_colors)))]
                color = map_color(x, y)

                # Draw the polygon
                pygame.draw.circle(screen, color, (x, y), size)
                # polygon(screen, color, x, y, 1.5 * size, 4)
        #flipping the cam but its important else we dont see anything(black screen)
        pygame.display.flip()
        #FPS
        clock.tick(60)
    #QUITING!
    cv2.destroyAllWindows()
    cap.release()
    pygame.quit()

#to open the app !
Track_Motion()