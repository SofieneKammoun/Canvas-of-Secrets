# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:58:26 2023

@author: Sofiene
"""

import pygame
from pygame.locals import QUIT
import random
import math
import numpy as np
from pygame import mixer
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
NUM_PARTICLES = 4000
MICROPHONE_THRESHOLD = 2# Adjust as needed

# Create a Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Visualization")

# Initialize particles
particles = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_PARTICLES)]
images=[]
current_word=""
is_word_detected = False
for i in range(0,7):
    letter = chr(ord('A')+i)
    name = 'noteBG/'+letter+'.png'
    image = pygame.image.load(name).convert()
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))  # Resize to match canvas size
    images.append(image)

#name = 'noiseTexture/noiseTexture C.png'
#image = pygame.image.load(name).convert()
#image = pygame.transform.scale(image, (WIDTH, HEIGHT))  # Resize to match canvas size
i=1

# Pygame clock
color = (random.randint(0, 200), random.randint(50, 150), random.randint(50, 155))
clock = pygame.time.Clock()

note = ''
key_mapping = {
    'Q': 'C3',
    'S': 'D3',
    'D': 'E3',
    'F': 'F3',
    'G': 'G3',
    'H': 'A3',
    'J': 'B3',
    'K': 'C4',
    'L': 'D4',
    'M': 'E4'
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
         # Check for a specific word, for example, "hello"
             current_word += event.unicode.lower()
             note = key_mapping.get(event.unicode.upper(), '')
             if note : 
                 sound_file_name= 'wav/'+ note + '.wav'
                 sound = mixer.Sound(sound_file_name)
                 sound.play()
             if "code" in current_word:
                 print("done")
                 is_word_detected = True
                 current_word=""
    # Create a background color with reduced alpha value (e.g., 200 for semi-transparency)
    rcolor = random.randint(10, 25)
    gcolor = random.randint(5, 20)
    bcolor = random.randint(6, 20)
    background_color = (rcolor, gcolor, bcolor)
    alpha_value = 5
    # Set the alpha value (transparency)
    # Create a new surface with the desired background color and alpha
    background_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    pygame.draw.rect(background_surface, background_color + (alpha_value,), (0, 0, WIDTH, HEIGHT))
    # Blit the background surface onto the main screen
    screen.blit(background_surface, (0, 0))
    

    for p in range(len(particles)):
     if p < len(particles):
        x, y = particles[p]
     else :
         break
     if is_word_detected == False :
        if note :
            if not (0 <= x < WIDTH) or not (0 <= y < HEIGHT):
                x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            normalized_x = (x / WIDTH) % 1.0
            normalized_y = (y / HEIGHT) % 1.0
            # Sample the grayscale value from the image at the normalized positions
            i = ord(note[0])-ord('A')
            gray_value = images[i].get_at((int(normalized_x * image.get_width()), int(normalized_y * image.get_height()))).r / 255.0
            #gray_value = image.get_at((int(normalized_x * image.get_width()), int(normalized_y * image.get_height()))).r / 255.0
            a =  12* math.pi * gray_value
            x += 2* math.cos(a)
            y += 2* math.sin(a)
            particles[p]= (x,y)
            pygame.draw.circle(screen, color, (int(x), int(y)), 1)

        else:
            if not (0 < x < WIDTH) or not (0 < y <= HEIGHT):
                x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            angle = random.uniform(0, 2 * 3.14159)
            x +=  5  * math.cos(angle)
            y +=  5 * math.sin(angle)
             
            # Draw particles with random colors
            particles[p]= (x,y)
            color = (random.randint(0,255), random.randint(0, 255), random.randint(0,255))
            pygame.draw.circle(screen, color, (int(x), int(y)),1.2 )
            
            
     else :
         dis=math.sqrt(math.pow(HEIGHT/2 - y,2)+math.pow(WIDTH/2 - x,2))
         dis=10 +1/dis
         a = math.atan2(HEIGHT/2 - y, WIDTH/2 - x)
         x += dis* math.cos(a)
         y += dis* math.sin(a)
         particles[p]= (x,y)
         pygame.draw.circle(screen, color, (int(x), int(y)), 1)
         if random.randint(0, 100)<5:
             particles.pop(p)
         
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
