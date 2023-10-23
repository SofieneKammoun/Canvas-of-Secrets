# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:51:53 2023

@author: Sofiene
"""

import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
NUM_IMAGES = 11
image_size = (1920, 1080)  # Set to the size of your images
notes_dir = "notes"
output_dir = "noteBG"  # Output directory for the generated images

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)
file_list = os.listdir(notes_dir)
# Load the code image


for note_file in file_list:
    # Load a random noiseTexture image

    note_image = pygame.image.load(os.path.join(notes_dir, note_file))

    # Random position
    x = 500
    y = 100
    
    # Resize the code image

    
    # Create a new surface for the result
    result_image = pygame.Surface(image_size)
    pygame.draw.rect(result_image, (255,255,255) , (0, 0 , 1920, 1080))
    # Fill with noiseTexture
    

    # Overlay the code image
    result_image.blit(note_image, (x, y))

    # Save the resulting image to the output directory
    output_path =f"{output_dir}/{note_file[0]}.png"


    pygame.image.save(result_image, output_path)
    print("Note-image is generated")

# Quit Pygame
pygame.quit()
