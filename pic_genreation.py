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
image_size = (1080, 720)  # Set to the size of your images
code_image_path = "code.png"
noise_texture_dir = "noiseTexture"
output_dir = "output"  # Output directory for the generated images

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load the code image
code_image = pygame.image.load(code_image_path)

for i in range(NUM_IMAGES):
    # Load a random noiseTexture image
    noise_texture_file = random.choice(os.listdir(noise_texture_dir))
    noise_texture_image = pygame.image.load(os.path.join(noise_texture_dir, noise_texture_file))

    # Random position
    x = random.randint(0,800)
    y = random.randint(0 ,300)
    angle = random.uniform(-20, 20)
    # Random size
    scale_factor = random.uniform(0.5, 0.8)
    new_width = int(code_image.get_width() * scale_factor)
    new_height = int(code_image.get_height() * scale_factor)

    # Resize the code image
    code_image_scaled = pygame.transform.scale(code_image, (new_width, new_height))
    code_image_rotated = pygame.transform.rotate(code_image_scaled, angle)
    # Create a new surface for the result
    result_image = pygame.Surface(image_size)

    # Fill with noiseTexture
    result_image.blit(noise_texture_image, (0, 0))

    # Overlay the code image
    result_image.blit(code_image_rotated, (x, y))

    # Save the resulting image to the output directory
    output_path = os.path.join(output_dir, f"output_image_{i}.png")
    pygame.image.save(result_image, output_path)
    print("image done")

# Quit Pygame
pygame.quit()
