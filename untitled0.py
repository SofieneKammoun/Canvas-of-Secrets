import pygame
from pygame.locals import QUIT
import random
import math
import sounddevice as sd
import numpy as np
from perlin_noise import PerlinNoise

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
NUM_PARTICLES = 4000
MICROPHONE_THRESHOLD = 1# Adjust as needed

# Create a Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Visualization")

# Initialize particles
particles = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_PARTICLES)]
images=[]

for i in range(0,10):
    name = 'output/output_image_'+str(i)+'.png'
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

# Initialize microphone input
mic_data = []

def audio_callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    mic_data.extend(indata[:, 0])  # Extract the left channel data

sd.InputStream(callback=audio_callback, channels=2, dtype=np.float32, samplerate=44000).start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    # Create a background color with reduced alpha value (e.g., 200 for semi-transparency)
    rcolor = random.randint(10, 25)
    gcolor = random.randint(5, 20)
    bcolor = random.randint(6, 20)
    background_color = (rcolor, gcolor, bcolor)
    alpha_value = 10
    # Set the alpha value (transparency)
    # Create a new surface with the desired background color and alpha
    background_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    pygame.draw.rect(background_surface, background_color + (alpha_value,), (0, 0, WIDTH, HEIGHT))
    # Blit the background surface onto the main screen
    screen.blit(background_surface, (0, 0))

    if mic_data:
        mic_level = mic_data[-1]*150
    else:
        mic_level = 0.0

    for p in range(NUM_PARTICLES):
        x, y = particles[p]

        if mic_level> MICROPHONE_THRESHOLD :
            i= random.randint(0,9) 
            if not (0 < x < WIDTH) or not (0 < y <= HEIGHT):
                x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            angle = random.uniform(0, 2 * 3.14159)
            x += mic_level * 2  * math.cos(angle)
            y += mic_level * 2* math.sin(angle)
              
            # Draw particles with random colors
            particles[p]= (x,y)
            color = (random.randint(0,255), random.randint(0, 255), random.randint(0,255))
            pygame.draw.circle(screen, color, (int(x), int(y)),1.2 )

        else:
            
            if not (0 <= x < WIDTH) or not (0 <= y < HEIGHT):
                x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            normalized_x = (x / WIDTH) % 1.0
            normalized_y = (y / HEIGHT) % 1.0
            # Sample the grayscale value from the image at the normalized positions
            gray_value = images[i].get_at((int(normalized_x * image.get_width()), int(normalized_y * image.get_height()))).r / 255.0
            #gray_value = image.get_at((int(normalized_x * image.get_width()), int(normalized_y * image.get_height()))).r / 255.0
            a =  4.525* math.pi * gray_value
            x += 1* math.cos(a)
            y += 1* math.sin(a)
            particles[p]= (x,y)
            pygame.draw.circle(screen, color, (int(x), int(y)), 1.2)

    pygame.display.flip()
    clock.tick(80)

pygame.quit()
