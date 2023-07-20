import pygame

WIDTH, HEIGHT = 1000, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Froggers")

background = pygame.image.load('Images/BG City.jpg').convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

frog = pygame.image.load('Images/frog.png').convert_alpha()
frog = pygame.transform.scale(frog, (150, 150))

car = pygame.image.load('Images/car.png').convert_alpha()
car = pygame.transform.scale(car, (120, 120))

snake = pygame.image.load('Images/snake.png').convert_alpha()
snake = pygame.transform.scale(snake, (120, 120))

log_image = pygame.image.load('Images/log.png').convert_alpha()
log_image = pygame.transform.scale(log_image, (200, 80))

class Log:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.speed < 0 and self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.speed > 0 and self.rect.left > WIDTH:
            self.rect.right = 0
        
# Create log objects
log_image = pygame.image.load('Images/log.png').convert_alpha()
log_image = pygame.transform.scale(log_image, (200, 80))

log1 = Log(log_image, WIDTH + 200, 250, -4)
log2 = Log(log_image, -200, 350, 3)
log3 = Log(log_image, WIDTH + 400, 150, 4)
logs = [log1, log2, log3]

def draw_window():
    global WIDTH
    background_width = background.get_rect().width
    background_offset = WIDTH % background_width

    SCREEN.blit(background, (background_offset - background_width, 0))
    if background_offset < WIDTH:
        SCREEN.blit(background, (background_offset, 0))

    WIDTH -= -1

    # Draw logs
    for log in logs:
        SCREEN.blit(log.image, log.rect)

    # Draw characters
    SCREEN.blit(frog, (300, 420))
    SCREEN.blit(car, (460, 460))
    SCREEN.blit(snake, (650, 500))

    pygame.display.update()

def main():
    pygame.init()
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for log in logs:
            log.update()

        draw_window()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()