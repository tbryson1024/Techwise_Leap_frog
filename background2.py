import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display dimensions
width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    display.fill(white)

    # Your game drawing and logic here

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # 60 FPS

# Clean up and quit Pygame
pygame.quit()
sys.exit()
