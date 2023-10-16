# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:39:00 2023

@author: Sofiene
"""

import pygame
import random
# Initialize Pygame
pygame.init()
width = 1200
height = 780
# Create a Pygame screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Keyboard Input Example")

# Define a Boolean variable
is_word_detected = False
current_word =""
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Check for a specific word, for example, "hello"
            angle = random.uniform(-50, 20)
            key = event.unicode
            font = pygame.font.Font(None, random.randint(80, 180))
            text = font.render(key.lower() ,True, (0, 0, 0),(255,255, 255))
            rotated_text = pygame.transform.rotate(text, angle)

            # Get a random position within the screen boundaries
            x = random.randint(0, width - rotated_text.get_width())
            y = random.randint(0, height - rotated_text.get_height())

            # Display the rotated text on the screen
            screen.blit(rotated_text, (x, y))
            current_word += event.unicode.lower()
            if "hello" in current_word:
                print("done")
                current_word=""
                


    # Clear the screen
    
    background_color = (100 , 200  , 230)
    alpha_value = 50
    # Set the alpha value (transparency)
    # Create a new surface with the desired background color and alpha
    background_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    background_surface.set_alpha(alpha_value)
    pygame.draw.rect(background_surface, background_color , (0, 0,width, height))
    # Blit thescreen background surface onto the main 
    screen.blit(background_surface, (0, 0))
    # Draw a message based on the Boolean variable
    if is_word_detected:
        font = pygame.font.Font(None, 36)
        text = font.render("Word Detected: Hello!", True, (0, 0, 0))
        screen.blitz(text, (200, 200))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
