import pygame

WIDTH, HEIGHT = 1000, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Froggers")


background = pygame.image.load('BG City.jpg').convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


frog = pygame.image.load('frog.png').convert_alpha()
frog = pygame.transform.scale(frog, (150, 150))

car = pygame.image.load('car.png').convert_alpha()
car = pygame.transform.scale(car, (120, 120))

snake = pygame.image.load('snake.png').convert_alpha()
snake = pygame.transform.scale(snake, (120, 120))



def draw_window():
    global WIDTH  # Declare WIDTH as global to modify its value

    background_width = background.get_rect().width
    background_offset = WIDTH % background_width

    SCREEN.blit(background, (background_offset - background_width, 0))
    if background_offset < WIDTH:
        SCREEN.blit(background, (background_offset, 0))

    WIDTH -= -1  # Update for continuous movement

    # Draw characters
    SCREEN.blit(frog, (300, 420))
    SCREEN.blit(car, (460, 460))
    SCREEN.blit(snake,(650,500))

    pygame.display.update()

def main():
    pygame.init()
   
    run = True
    while run:
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()