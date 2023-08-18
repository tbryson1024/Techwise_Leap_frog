import pygame
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
from pygame import Surface, mixer, sprite
=======
from pygame import Surface, mixer
>>>>>>> 1d9bfbf (Adding logs to new main code and backgrounds):car moving1.py
=======
from pygame import Surface, mixer, sprite
>>>>>>> 856efea (Removed logs from first screen.):car moving1.py
import sys
import random
import menu

menu.main()

pygame.init()
pygame.mixer.init(devicename='directsound')
clock = pygame.time.Clock()

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
current_level = 1
=======
show_logs = False
>>>>>>> 1d9bfbf (Adding logs to new main code and backgrounds):car moving1.py

=======
>>>>>>> e62f4f0 (Saving changes to logs3):car moving1.py
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Leap Frog')

road_bg = pygame.image.load('Images/road2.jpg').convert()
road_bg = pygame.transform.scale(road_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

swamp_bg = pygame.image.load('Images/bg1.png').convert()
swamp_bg = pygame.transform.scale(swamp_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

BG_ROAD_SIZE = 1080

BG_SWAMP_SIZE = 1080

current_background = pygame.image.load('Images/road2.jpg').convert()
current_background = pygame.transform.scale(current_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
<<<<<<< HEAD:leap_frog.py


#mixer.music.load("Images/Swamps Nature.wav")
mixer.music.load("Images/mixkit-subway-old-depart-ambience-2679.wav")
mixer.music.play(-1)  # play non-stop


<<<<<<< HEAD



if current_level == 1:
    mixer.music.load("Images/mixkit-subway-old-depart-ambience-2679.wav")
    mixer.music.play(-1)  # play non-stop

if current_level == 2:
    mixer.music.load("Images/Swamps Nature.wav")
    mixer.music.play(-1)  # play non-stop
=======
>>>>>>> 1d9bfbf (Adding logs to new main code and backgrounds):car moving1.py

<<<<<<< HEAD:leap_frog.py
=======
#mixer.music.load("Images/Swamps Nature.wav")
<<<<<<< HEAD:leap_frog.py
mixer.music.load("Images/mixkit-subway-old-depart-ambience-2679.wav")
mixer.music.play(-1)  # play non-stop
>>>>>>> 9bcd7ea (add new sound):car moving1.py
=======
#mixer.music.load("Images/mixkit-subway-old-depart-ambience-2679.wav")
#mixer.music.play(-1)  # play non-stop


road_sound = mixer.music.load("Images/mixkit-subway-old-depart-ambience-2679.wav")
mixer.music.play()
#swamp_sound = mixer.music.load("Images/mixkit-insects-birds-and-frogs-in-the-swamp-ambience-40.wav")
#dead_sound = mixer.music.load("Images/mixkit-futuristic-electronic-engine-fail-2941.wav")

#mixer.music.play(1)  # play non-stop
>>>>>>> 35d6b74 (add sounds to different levels):car moving1.py


=======
>>>>>>> 40ede70 (adding leap_frog.py)
class Player(pygame.sprite.Sprite):
    frog_position = [500, 675]  # Initial position of the frog

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.health = 100  # health bar start width
        self.lives = 1  # number of lives
        self.alive = True
        self.is_animating = False
        self.directions = ["right", "left", "up", "down"]
        self.frog_sprites = {direction: [] for direction in self.directions}

        for direction in self.directions:
            for i in range(1, 7):
                image_path = f'Images/frog-{direction}{i}.png'
                sprite = pygame.image.load(image_path).convert()
                sprite.set_colorkey((0, 0, 0))
                sprite = pygame.transform.scale(sprite, (50, 50))
                self.frog_sprites[direction].append(sprite)

        self.current_sprite = 0
        self.image = self.frog_sprites["right"][self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.direction = "up"

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
=======
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
    def move(self, dx, dy):
        self.frog_position[0] += dx  # Update horizontal coordinate
        self.frog_position[1] += dy  # Update vertical coordinate
        self.rect.topleft = self.frog_position
<<<<<<< HEAD:leap_frog.py
=======
        self.frog_sprites = [self.sprites_right,self.sprites_left,self.sprites_up,self.sprites_down]

        self.on_log = False
        
        for direction_sprites in self.frog_sprites:
            for i in range(len(direction_sprites)):
                direction_sprites[i].set_colorkey((0, 0, 0))
                direction_sprites[i] = pygame.transform.scale(direction_sprites[i], (50, 50))

      
>>>>>>> 856efea (Removed logs from first screen.):car moving1.py
=======
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py

    def move_right(self):
        if self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.direction = "right"
            self.move(3, 0)

    def move_left(self):
        if self.rect.x > 0:
            self.direction = "left"
            self.move(-3, 0)

    def move_up(self):
        if self.rect.y > 0:
            self.direction = "up"
            self.move(0, -3)

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.direction = "down"
            self.move(0, 3)

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
=======
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.frog_position[0] += dx  # Update horizontal coordinate
        self.frog_position[1] += dy  # Update vertical coordinate
        self.rect.topleft = self.frog_position

>>>>>>> e62f4f0 (Saving changes to logs3):car moving1.py
=======
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
    def animate(self):
        self.is_animating = True

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.animate()
            self.move_right()
        elif keys[pygame.K_LEFT]:
            self.animate()
            self.move_left()
        elif keys[pygame.K_UP]:
            self.animate()
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.animate()
            self.move_down()

    def health_bar(self, screen):
        health_bar_width = 100
        health_bar_height = 10
        health_bar_x = self.rect.x  # horizontal position of the health bar
        health_bar_y = self.rect.y - 30  # vertical position of the health bar

        pygame.draw.rect(screen, (255, 0, 0),
                         (health_bar_x, health_bar_y, health_bar_width, health_bar_height))  # Background bar
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, self.health, health_bar_height))  # Health bar

    def update(self, speed=0.1):
        self.movement()

        if self.is_animating:
            self.current_sprite += speed
            if self.current_sprite >= len(self.frog_sprites[self.direction]):
                self.current_sprite = 0
                self.is_animating = False

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
        self.image = self.frog_sprites[self.direction][int(self.current_sprite)]
=======
        # Check if the player is on a log
        on_log = False
        for log in log1, log2, log3:
            if pygame.sprite.collide_mask(self, log):
                on_log = True
                if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]):
                    log.carry_player(self)  # Move the player with the log

        # Update the frog's position based on movement and log interaction
        if not on_log:
            if self.direction == "right":
                self.image = self.sprites_right[int(self.current_sprite)]
            elif self.direction == "left":
                self.image = self.sprites_left[int(self.current_sprite)]
            elif self.direction == "up":
                self.image = self.sprites_up[int(self.current_sprite)]
            elif self.direction == "down":
                self.image = self.sprites_down[int(self.current_sprite)]

<<<<<<< HEAD:leap_frog.py
>>>>>>> e62f4f0 (Saving changes to logs3):car moving1.py
        self.rect.topleft = self.frog_position
=======
       # Not needed as is - self.rect.topleft = self.frog_position
>>>>>>> 856efea (Removed logs from first screen.):car moving1.py
=======
        self.image = self.frog_sprites[self.direction][int(self.current_sprite)]
        self.rect.topleft = self.frog_position
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def reset_player(self):
<<<<<<< HEAD
<<<<<<< HEAD:leap_frog.py
=======
#        self.frog_position = [500, 675]  # Initial position of the frog
#        self.rect.topleft = self.frog_position
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
=======
>>>>>>> 40ede70 (adding leap_frog.py)
        self.direction = "up"
        self.health = 100
        self.lives = 1
        self.alive = True

<<<<<<< HEAD:leap_frog.py
    def reset_pos(self):
       self.frog_position = [500, 675]  # Initial position of the frog
       self.rect.topleft = self.frog_position



=======
>>>>>>> ce4576c (adding cave 4):car moving1.py
    def reset_pos(self):
       self.frog_position = [500, 675]  # Initial position of the frog
       self.rect.topleft = self.frog_position



class Car(pygame.sprite.Sprite):
    def __init__(self, image_path, pos_x, pos_y, speed):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = speed
<<<<<<< HEAD
<<<<<<< HEAD:leap_frog.py
=======
        
>>>>>>> ce4576c (adding cave 4):car moving1.py
=======
<<<<<<< HEAD
        
=======
>>>>>>> c7147e1 (Updated caves)
>>>>>>> eb25d32 (Updated caves)

    def update(self):
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.left > SCREEN_WIDTH:
            self.reset_position()
        elif self.speed < 0 and self.rect.right < 0:
            self.reset_position()
        

    def reset_position(self):
        if self.speed > 0:
            self.rect.right = 0
        else:
            self.rect.left = SCREEN_WIDTH
    
    def get_mask(self):
        return pygame.mask.from_surface(self.image)

# Create cars
cars = pygame.sprite.Group()
car_images_right = [
     "Images/car3-right.png", "Images/car4-right.png", "Images/car5-right.png", "Images/car6-right.png"
]
car_images_left = [
    "Images/car1-left.png", "Images/car2-left.png", "Images/car3-left.png", "Images/car4-left.png", "Images/car5-left.png", "Images/car6-left.png"
]

# Cars 1 to 6 move from left to right
for i in range(3):
    image_path = car_images_right[i]
#    pos_x = -random.randint(200, 450)  # Starting offscreen from the left
    pos_x = SCREEN_WIDTH + random.randint(100, 460)
    pos_y = 90 + i * 135  # Adjust the spacing between cars
    speed = random.randint(7, 14)  # Random speed 
    car = Car(image_path, pos_x, pos_y, speed)
    car.image = pygame.image.load(image_path).convert()  # Load the image
    car.image.set_colorkey((0, 0, 0))  # Remove the black background
    car.image = pygame.transform.scale(car.image, (145, 145))  # Scale the image to the desired dimensions
    cars.add(car)

# Cars 7 to 12 move from right to left
for i in range(4):
    image_path = car_images_left[i]
    pos_x = SCREEN_WIDTH + random.randint(120, 470)  # Starting offscreen from the right
    pos_y = 210 + i * 120  # Adjust the spacing between cars
    speed = -random.randint(9, 12)  # Random  speed 
    car = Car(image_path, pos_x, pos_y, speed)
    car.image = pygame.image.load(image_path).convert()  # Load the image
    car.image.set_colorkey((0, 0, 0))  # Remove the black background
    car.image = pygame.transform.scale(car.image, (145, 145))  # Scale the image to the desired dimensions
    cars.add(car)


class New_level(pygame.sprite.Sprite): # snippet of image on top of screen taking player to second background
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('Images/beginning level1.jpg').convert()
        self.image = pygame.transform.scale(self.image, (1090, 260))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
    
    current_level = 2

=======

<<<<<<< HEAD
       
<<<<<<< HEAD
>>>>>>> 35d6b74 (add sounds to different levels):car moving1.py
=======
=======
>>>>>>> 0823d0d (adding leap_frog.py)
>>>>>>> 40ede70 (adding leap_frog.py)
    def update(self):
        screen.blit(self.image, self.rect)
=======
      
       
<<<<<<< HEAD:leap_frog.py
#    def update(self):
#        screen.blit(self.image, self.rect)
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
=======
    def update(self):
        screen.blit(self.image, self.rect)
>>>>>>> ce4576c (adding cave 4):car moving1.py

    def get_mask(self):
        return pygame.mask.from_surface(self.image)


class Lake(pygame.sprite.Sprite): # snippet of lake image on top of background
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('Images/lake.png').convert()
        self.image = pygame.transform.scale(self.image, (1080, 390))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.layer = 1
      
    def update(self):
        screen.blit(self.image, self.rect)


class Gator(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        
        self.sprites = []
        self.is_animating = True
        self.sprites.append(pygame.image.load('Images/gator-right1.png').convert())
        self.sprites.append(pygame.image.load('Images/gator-right2.png').convert())
        self.sprites.append(pygame.image.load('Images/gator-right3.png').convert())
        self.sprites.append(pygame.image.load('Images/gator-right4.png').convert())
        self.sprites.append(pygame.image.load('Images/gator-left1.png').convert())
        self.sprites.append(pygame.image.load('Images/gator-left2.png').convert())
        self.sprites.append(pygame.image.load('Images/gator-left3.png').convert())
        self.sprites.append(pygame.image.load('Images/gator-left4.png').convert())
      
        # Set color to be removed for each loaded image
        for i in range(len(self.sprites)):
            self.sprites[i].set_colorkey((255, 255, 255))
            # Control the image size
            self.sprites[i] = pygame.transform.scale(self.sprites[i], (100, 100))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.speed = random.randrange(1, 4)

    def animate(self):
        self.is_animating = True

    def update(self, speed=0.1):
        if self.is_animating:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = True

            self.rect.x += self.speed
            if self.rect.right > SCREEN_WIDTH:
                self.rect.x = -self.rect.width 
                #self.rect.y = SCREEN_HEIGHT - self.rect.height  # Reset the position at the bottom of the screen
                self.rect.y = pos_y
                self.speed = random.randrange(1, 4)

            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.rect.x += self.speed
            if self.rect.right > SCREEN_WIDTH:
                self.kill()

<<<<<<< HEAD:leap_frog.py
=======

>>>>>>> ce4576c (adding cave 4):car moving1.py
    def get_mask(self):
        return pygame.mask.from_surface(self.image)

<<<<<<< HEAD
<<<<<<< HEAD
class LilyPad(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('Images/LilyPad.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.animation_timer = 0
        self.animation_speed = 5

    def update(self):
        self.animation_timer += 1
        if self.animation_timer > self.animation_speed:
            self.animation_timer = 0
            self.rect.y += random.uniform(-1, 1)


=======
=======

>>>>>>> c7147e1 (Updated caves)
class Log(pygame.sprite.Sprite):
    def __init__(self, image_path, pos_x, pos_y, speed):
        super().__init__()
        self.image_path = pygame.image.load(image_path).convert()
        self.image = self.image_path
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
<<<<<<< HEAD
        self.speed = random.randrange(1,4)  
=======
        self.speed = speed
>>>>>>> f6467cc (Added more logs)
        self.player = None  # Player attribute
        self.image = pygame.transform.scale(self.image, (150, 75))
        self.image.set_colorkey((0, 0, 0))

    def set_player(self, player):
        self.player = player

    def update(self):
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.left > SCREEN_WIDTH:
            self.reset_position()
        elif self.speed < 0 and self.rect.right < 0:
            self.reset_position()

    def reset_position(self):
        if self.speed > 0:
            self.rect.right = 0
        else:
            self.rect.left = SCREEN_WIDTH

    def carry_player(self, player):
       player.frog_position[0] += self.speed  # Adjust the frog's position based on the log's speed
       player.rect.topleft = player.frog_position

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
    
player = Player(Player.frog_position[0], Player.frog_position[1])
""" log1.set_player(player)
log2.set_player(player)
<<<<<<< HEAD
log3.set_player(player)
>>>>>>> 1b9f87d (Adding logs to new main code and backgrounds)
=======
log3.set_player(player) """

>>>>>>> 33821d4 (Saving changes)

<<<<<<< HEAD:leap_frog.py
class LilyPad(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('Images/LilyPad.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.animation_timer = 0
        self.animation_speed = 5

    def update(self):
        self.animation_timer += 1
        if self.animation_timer > self.animation_speed:
            self.animation_timer = 0
            self.rect.y += random.uniform(-1, 1)


class Log(pygame.sprite.Sprite):
    def __init__(self, image_path, pos_x, pos_y, speed):
        super().__init__()
        self.image_path = pygame.image.load(image_path).convert()
        self.image = self.image_path
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
<<<<<<< HEAD
        self.speed = speed
=======
        self.speed = speed  
>>>>>>> 675536f (Adding more logs)
        self.player = None  # Player attribute
        self.image = pygame.transform.scale(self.image, (150, 75))
        self.image.set_colorkey((0, 0, 0))
    def set_player(self, player):
        self.player = player

    def update(self):
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.left > SCREEN_WIDTH:
            self.reset_position()
        elif self.speed < 0 and self.rect.right < 0:
            self.reset_position()

    def reset_position(self):
        if self.speed > 0:
            self.rect.right = 0
        else:
            self.rect.left = SCREEN_WIDTH

    def carry_player(self, player):
       player.frog_position[0] += self.speed  # Adjust the frog's position based on the log's speed
       player.rect.topleft = player.frog_position

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
    
player = Player(Player.frog_position[0], Player.frog_position[1])
<<<<<<< HEAD
=======

>>>>>>> 675536f (Adding more logs)

=======
>>>>>>> ce4576c (adding cave 4):car moving1.py
class Health_bar:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
        self.health_bar_width = 100
        self.health_bar_height = 20
        self.health_bar_x = 10  # horizontal position of the health bar
        self.health_bar_y = 10  # vertical position of the health bar

<<<<<<< HEAD

<<<<<<< HEAD:leap_frog.py
=======
>>>>>>> 675536f (Adding more logs)
=======
>>>>>>> ce4576c (adding cave 4):car moving1.py
    def draw_health_bars(self):
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.health_bar_x, self.health_bar_y, self.health_bar_width, self.health_bar_height))  # Background bar
        pygame.draw.rect(self.screen, (0, 255, 0),
                         (self.health_bar_x, self.health_bar_y, self.player.health, self.health_bar_height))  # Health bar
     
       # Player Health display
        if not self.player.alive:
            self.screen.fill((0, 0, 0))
            #game_over_sound = mixer.Sound("game over.wav")
           # game_over_sound.play()
            #game_over = pygame.image.load('game over.jpg').convert()
            #game_over_rect = game_over.get_rect()
            #game_over_rect.center = (500, 300)
            font1 = pygame.font.Font('freesansbold.ttf', 35)
            text1 = font1.render('Press SPACE to restart', True, (255, 255, 255))
            text1Rect = text1.get_rect()
            text1Rect.bottom = 550
            text1Rect.left = 350
           # self.screen.blit(game_over, game_over_rect)
            self.screen.blit(text1, text1Rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
               player.alive = True
               player.lives = 1
               player.health = 100
               player.frog_position = [500, 675]  # Reset the player's position
               player.rect.topleft = player.frog_position
               player.direction = "up"
<<<<<<< HEAD

<<<<<<< HEAD
               #Clear the cave frog
            cave_frog_sprites.empty()


=======
       
=======
               #Clear the cave frog
            cave_frog_sprites.empty()

>>>>>>> c7147e1 (Updated caves)
>>>>>>> eb25d32 (Updated caves)
        #Print Lives to screen
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render('Lives: ' + str(player.lives), True, (0,0,0))
        screen.blit(text,(650,20))

    def update(self):
        self.draw_health_bars()

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
=======
>>>>>>> ce4576c (adding cave 4):car moving1.py
class Caves(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image_path,scale_x, scale_y):
        super().__init__()

        self.image = pygame.image.load(image_path).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.image = pygame.transform.scale(self.image, (scale_x, scale_y))
=======

class Caves(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image_path,scale_x, scale_y):
        super().__init__()

        self.image = pygame.image.load(image_path).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
<<<<<<< HEAD:leap_frog.py

>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
=======
        self.image = pygame.transform.scale(self.image, (scale_x, scale_y))
>>>>>>> b885374 (add the fourth cave):car moving1.py

    def update(self):
        screen.blit(self.image, self.rect)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
    

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
=======

>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
=======
>>>>>>> ce4576c (adding cave 4):car moving1.py
class CaveFrog(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('Images/cave frog.png').convert()
        self.image = pygame.transform.scale(self.image, (50, 55))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.visible = False  # Initial visibility of cave frog
    
    def get_mask(self):
        return pygame.mask.from_surface(self.image)

<<<<<<< HEAD:leap_frog.py

<<<<<<< HEAD:leap_frog.py
# Initialize objects
=======
 # Initialize objects
>>>>>>> ce4576c (adding cave 4):car moving1.py
new_level = New_level(-10, -70)
=======
 # Initialize objects
<<<<<<< HEAD:leap_frog.py
new_level = New_level(0, 0)
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
=======
new_level = New_level(-10, -70)
>>>>>>> 5167da6 (fix frog/cave collision):car moving1.py
lake = Lake(-2, 255)

alligator = Gator(100, 500)
health_bar = Health_bar(player, screen)
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py

<<<<<<< HEAD
=======
cave1 = Caves(-70,-8)
cave2 = Caves(50,-8)
cave3 = Caves(170, -8)

cave_frog1= CaveFrog(103,180)
cave_frog2 = CaveFrog(217,180)
cave_frog3= CaveFrog(345,180)



# Create sprite groups with order of apperance 
>>>>>>> 675536f (Adding more logs)
=======
=======
<<<<<<< HEAD
>>>>>>> 856efea (Removed logs from first screen.):car moving1.py
lilypads=LilyPad (100,200)
# Create sprite groups with ordem of apperance 
>>>>>>> a875787 (saving changes):car moving1.py
background_sprites = pygame.sprite.LayeredUpdates()
<<<<<<< HEAD:leap_frog.py
background_sprites.add(background_sprites, cars)

player_sprites = pygame.sprite.LayeredUpdates()
<<<<<<< HEAD
player_sprites.add(player)
=======
player_sprites.add(player) 
>>>>>>> 675536f (Adding more logs)
=======
background_sprites.add(background_sprites,cars, new_level)  # Background sprites should be drawn first
=======

<<<<<<< HEAD
cave1 = Caves(-90, -20, 'Images/minicave.png',420,420)
cave2 = Caves(50, -20, 'Images/minicave.png',420,420)
cave3 = Caves(170, -20, 'Images/minicave.png',420,420)
cave4 = Caves(300, -55, 'Images/main cave.png',600, 320) 

cave_frog1= CaveFrog(88,180)
cave_frog2 = CaveFrog(217,180)
cave_frog3= CaveFrog(345,180)
cave_frog4 = CaveFrog(600,150)

=======
>>>>>>> c7147e1 (Updated caves)

<<<<<<< HEAD

# Create sprite groups with order of apperance 
<<<<<<< HEAD
sprites = pygame.sprite.Group() #Create Sprites Group
>>>>>>> c3fde22 (Removed logs from first screen.)
=======
#sprites = pygame.sprite.Group() #Create Sprites Group

#background_sprites = pygame.sprite.LayeredUpdates()
#sprites.add(background_sprites,cars, new_level)  # Background sprites should be drawn first

#alligators_group = pygame.sprite.Group()

#car_sprites = pygame.sprite.LayeredUpdates()
#car_sprites.add(cars)  # Cars should be drawn on top of player and background

#lake_sprites = pygame.sprite.LayeredUpdates()
#sprites.add(lake_sprites)

#player = Player(Player.frog_position[0], Player.frog_position[1])
#sprites.add(player) #Add player last to keep on top

#all_sprites = pygame.sprite.LayeredUpdates()
#all_sprites.add(player, alligators_group, cave1,cave2,cave3)
>>>>>>> 8c91984 (add caves, add collision detection frog/caves)

=======
>>>>>>> 0aa13e0 (adding cave 4)
background_sprites = pygame.sprite.LayeredUpdates()
background_sprites.add(background_sprites, cars) 

player_sprites = pygame.sprite.LayeredUpdates()
player_sprites.add(player) 

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
alligators_group = pygame.sprite.Group()
>>>>>>> 856efea (Removed logs from first screen.):car moving1.py
=======
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py

car_sprites = pygame.sprite.LayeredUpdates()
car_sprites.add(cars)
=======
car_sprites = pygame.sprite.LayeredUpdates()
car_sprites.add(cars)  
>>>>>>> ce4576c (adding cave 4):car moving1.py

lake_sprites = pygame.sprite.LayeredUpdates()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD

<<<<<<< HEAD
lilypad_sprites = pygame.sprite.LayeredUpdates()


log1 = Log("Images/log.png", 200, 250, 5)
log2 = Log("Images/log.png", 300, 500, 5)
log3 = Log("Images/log.png", 400, 350, -5)
log4 = Log("Images/log.png", 500, 550, -5)
log5 = Log("Images/log.png", 600, 400, 5)
log6 = Log("Images/log.png", 700, 300, 5)
log7 = Log("Images/log.png", 800, 600, -5)
log8 = Log("Images/log.png", 900, 450, -5)

log_sprites = pygame.sprite.LayeredUpdates()
log_sprites.add(log1, log2, log3, log4, log5, log6, log7, log8)
=======
log1 = Log("Images/log.png", 100, 350, -5)
log2 = Log("Images/log.png", 300, 350, -5)
log3 = Log("Images/log.png", 100, 400, 5)
log4 = Log("Images/log.png", 300, 400, 5)
log5 = Log("Images/log.png", 200, 450, -5)
log6 = Log("Images/log.png", 100, 450, -5)
log7 = Log("Images/log.png", 300, 500, 5)
log8 = Log("Images/log.png", 100, 500, 5)
log9 = Log("Images/log.png", 400, 550, -5)
log10 = Log("Images/log.png", 100, 550, -5)
log11 = Log("Images/log.png", 500, 600, 5)
log12 = Log("Images/log.png", 100, 600, 5)

log_sprites = pygame.sprite.LayeredUpdates()
log_sprites.add(log1, log2, log3, log4, log5, log6, log7, log8, log9, log10, log11, log12)
>>>>>>> 675536f (Adding more logs)

alligators_sprites = pygame.sprite.LayeredUpdates()
alligators_sprites.add(alligator)

logs_group = pygame.sprite.LayeredUpdates()
logs_group.add(log1, log2, log3)

all_sprites = pygame.sprite.LayeredUpdates()
<<<<<<< HEAD:leap_frog.py
all_sprites.add(background_sprites,car_sprites,player_sprites)
=======
all_sprites.add(background_sprites, player_sprites, car_sprites, log1, log2, log3)
>>>>>>> 1d9bfbf (Adding logs to new main code and backgrounds):car moving1.py

cave1 = Caves(-90, -20, 'Images/minicave.png',420,420)
cave2 = Caves(50, -20, 'Images/minicave.png',420,420)
cave3 = Caves(170, -20, 'Images/minicave.png',420,420)
cave4 = Caves(300, -55, 'Images/main cave.png',600, 320)
cave_sprites = pygame.sprite.LayeredUpdates()

cave_frog1= CaveFrog(88,180)
cave_frog2 = CaveFrog(217,180)
cave_frog3= CaveFrog(345,180)
cave_frog4 = CaveFrog(600,150)
cave_frog_sprites = pygame.sprite.LayeredUpdates()
=======
sprites.add(lake_sprites)

player = Player(Player.frog_position[0], Player.frog_position[1])
sprites.add(player) #Add player last to keep on top
>>>>>>> 856efea (Removed logs from first screen.):car moving1.py
=======

alligators_sprites = pygame.sprite.LayeredUpdates()
alligators_sprites.add(alligator)
=======
=======

>>>>>>> eb25d32 (Updated caves)
log1 = Log("Images/log.png", random.randint(100, 300), random.randint(300, 490), random.randint(5, 10))
log2 = Log("Images/log.png", random.randint(100, 300), random.randint(300, 490), random.randint(5, 10))
log3 = Log("Images/log.png", random.randint(100, 300), random.randint(300, 490), random.randint(5, 10))
>>>>>>> 646d051 (Saving changes)
=======
log1 = Log("Images/log.png", 200, 230, 5)
log2 = Log("Images/log.png", 250, 290, -5)
log3 = Log("Images/log.png", 500, 380, 5)
log4 = Log("Images/log.png", 650, 470, -5)
log5 = Log("Images/log.png", 730, 525, 5)
log6 = Log("Images/log.png", 850, 600, -5)
log7 = Log("Images/log.png", 500, 250,  5)
log8 = Log("Images/log.png", 730, 150, -5)

>>>>>>> 3050bc8 (Added more logs)

<<<<<<< HEAD
cave_fro_sprites = pygame.sprite.LayeredUpdates()
=======
log_sprites = pygame.sprite.LayeredUpdates()
<<<<<<< HEAD
log_sprites.add(log1, log2, log3)
>>>>>>> 1f515aa (Got frog on top of logs, now have to remove from screen 1 again.)
=======
log_sprites.add(log1, log2, log3, log4, log5, log6, log7, log8)
>>>>>>> f6467cc (Added more logs)


alligators_sprites = pygame.sprite.LayeredUpdates()
alligators_sprites.add(alligator)

<<<<<<< HEAD
<<<<<<< HEAD
=======
cave_frog_sprites = pygame.sprite.LayeredUpdates()

>>>>>>> 0823d0d (adding leap_frog.py)
=======
>>>>>>> c7147e1 (Updated caves)
all_sprites = pygame.sprite.LayeredUpdates()
all_sprites.add(background_sprites,car_sprites,player_sprites)

cave1 = Caves(-90, -20, 'Images/minicave.png',420,420)
cave2 = Caves(50, -20, 'Images/minicave.png',420,420)
cave3 = Caves(170, -20, 'Images/minicave.png',420,420)
cave4 = Caves(300, -55, 'Images/main cave.png',600, 320)
cave_sprites = pygame.sprite.LayeredUpdates()

cave_frog1= CaveFrog(88,180)
cave_frog2 = CaveFrog(217,180)
cave_frog3= CaveFrog(345,180)
cave_frog4 = CaveFrog(600,150)
cave_frog_sprites = pygame.sprite.LayeredUpdates()

<<<<<<< HEAD
<<<<<<< HEAD:leap_frog.py
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
=======
#cave_fro_sprites.add(player, background_sprites,cave_frog1,cave_frog2,cave_frog3,cave_frog4)
>>>>>>> ce4576c (adding cave 4):car moving1.py
=======
>>>>>>> 40ede70 (adding leap_frog.py)

scroll_x = 0
scroll_y = 0
  

#main Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
=======
>>>>>>> ce4576c (adding cave 4):car moving1.py
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 35d6b74 (add sounds to different levels):car moving1.py
=======
<<<<<<< HEAD
>>>>>>> 40ede70 (adding leap_frog.py)
=======
<<<<<<< HEAD
>>>>>>> 2ccb3e7 (adding leap_frog.py)
=======
<<<<<<< HEAD
>>>>>>> eb25d32 (Updated caves)
    player.update()
=======
=======

>>>>>>> 0823d0d (adding leap_frog.py)
=======
>>>>>>> 6ce169e (adding leap_frog.py)
=======
    player.update()
>>>>>>> c7147e1 (Updated caves)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Jump_sound = mixer.Sound("Images/jump.wav")
        Jump_sound.play()
        player.animate()
<<<<<<< HEAD
<<<<<<< HEAD
        player.move_right()
        
=======
        player.move_right
=======
        player.move_right()
>>>>>>> 6ce169e (adding leap_frog.py)

>>>>>>> 0823d0d (adding leap_frog.py)
    elif keys[pygame.K_LEFT]:
        Jump_sound = mixer.Sound("Images/jump.wav")
        Jump_sound.play()
        player.animate()
        player.move_left()

    elif keys[pygame.K_UP]:
        Jump_sound = mixer.Sound("Images/jump.wav")
        Jump_sound.play()
        player.animate()
        player.move_up()

    elif keys[pygame.K_DOWN]:
        Jump_sound = mixer.Sound("Images/jump.wav")
        Jump_sound.play()
        player.animate()
        player.move_down()

    if player.frog_position[0] >= BG_ROAD_SIZE:
       current_background = swamp_bg
<<<<<<< HEAD
       

    

<<<<<<< HEAD
>>>>>>> 33ff7ab (add sounds to different levels)
=======
=======
>>>>>>> 6ce169e (adding leap_frog.py)

>>>>>>> 0823d0d (adding leap_frog.py)

<<<<<<< HEAD
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Jump_sound = mixer.Sound("Images/jump.wav")
        Jump_sound.play()
        player.animate()
        player.move_right()

    elif keys[pygame.K_LEFT]:
        Jump_sound = mixer.Sound("Images/jump.wav")
        Jump_sound.play()
        player.animate()
        player.move_left()

    elif keys[pygame.K_UP]:
        Jump_sound = mixer.Sound("Images/jump.wav")
        Jump_sound.play()
        player.animate()
        player.move_up()

    elif keys[pygame.K_DOWN]:
        Jump_sound = mixer.Sound("Images/jump.wav")
        Jump_sound.play()
        player.animate()
        player.move_down()

    if player.frog_position[0] >= BG_ROAD_SIZE:
       current_background = swamp_bg

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
=======
    if show_logs:
        player.update()
=======
>>>>>>> e62f4f0 (Saving changes to logs3):car moving1.py
=======

    player.update()
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py

>>>>>>> 1d9bfbf (Adding logs to new main code and backgrounds):car moving1.py
    # Check for collision between player and cars
    for car in cars:
        if pygame.sprite.collide_mask(player, car):
=======

    # Check for collision between player and cars
    for car in cars:
        if pygame.sprite.collide_mask(player, car):
<<<<<<< HEAD
            #if player.health > 0:
                player.health -= 10 # Reduce player's health by 
=======
                player.health -= 10 # Reduce player's health by
>>>>>>> c7147e1 (Updated caves)
                if player.health == 0 and player.lives > 0:
                    player.lives -= 1
                    player.health = 100
                elif player.health == 0 and player.lives == 0:
                    player.alive = False
>>>>>>> eb25d32 (Updated caves)

<<<<<<< HEAD
<<<<<<< HEAD:leap_frog.py
            if player.health == 0 and player.lives > 0:
                player.lives -= 1
                player.health = 100
            elif player.health == 0 and player.lives == 0:
                player.alive = False

=======
        

    
>>>>>>> 35d6b74 (add sounds to different levels):car moving1.py
=======
<<<<<<< HEAD
        

    
=======
>>>>>>> 6ce169e (adding leap_frog.py)
>>>>>>> 2ccb3e7 (adding leap_frog.py)
      # Check for collision between player and new_level
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
    if pygame.sprite.collide_mask(player, new_level):
        current_level = 2
        player.reset_pos()
      
=======
    if player.rect.colliderect(new_level.rect):
        player.reset_pos()
        #all_sprites.update()
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
=======
    if pygame.sprite.collide_mask(player, new_level):
        player.reset_pos()
<<<<<<< HEAD
<<<<<<< HEAD
      
>>>>>>> ce4576c (adding cave 4):car moving1.py
        new_level.kill()
        lake = Lake(-2, 255)  # Create the Lake and its position x, y
        lake_sprites.add(lake)  # Add lake
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py

        lilypads = LilyPad(300,500) #creating lilypads in it's positions

        all_sprites.update()
        new_level.kill()
        
        cave1 = Caves(-90, -20, 'Images/minicave.png',420,420)
        cave2 = Caves(50, -20, 'Images/minicave.png',420,420)
        cave3 = Caves(170, -20, 'Images/minicave.png',420,420)
        cave4 = Caves(375, -55, 'Images/main cave.png',500, 320)
        cave_sprites = pygame.sprite.LayeredUpdates()
        cave_sprites.add(cave1, cave2, cave3, cave4)


        cave_frog1= CaveFrog(88,180)
        cave_frog2 = CaveFrog(217,180)
        cave_frog3= CaveFrog(345,180)
        cave_frog4 = CaveFrog(600,150)
        cave_frog_sprites = pygame.sprite.LayeredUpdates()
        
        all_sprites.add(alligators_sprites, lilypad_sprites, log_sprites, cave_sprites, cave_frog_sprites, player_sprites)

=======
        lilypads=LilyPad(300,500) #creating lilypads in it's positions
        all_sprites.add(background_sprites, player_sprites, alligators_sprites,lilypads)
>>>>>>> a875787 (saving changes):car moving1.py
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        lilypads=LilyPad(300,500) #creating lilypads in it's positions
        all_sprites.add(background_sprites, player_sprites, alligators_sprites,lilypads)
=======
        all_sprites.add(background_sprites, player_sprites, alligators_sprites, logs_group)
>>>>>>> 5bf9194 (Saving changes, frog now moves with log)
<<<<<<< HEAD:leap_frog.py
>>>>>>> a8b0e91 (Saving changes, frog now moves with log):car moving1.py
=======
=======
        sprites.add(background_sprites, alligator, log1, log2, log3)
        sprites.add(player)
>>>>>>> c3fde22 (Removed logs from first screen.)
<<<<<<< HEAD:leap_frog.py
>>>>>>> 856efea (Removed logs from first screen.):car moving1.py
=======
=======
#        sprites.add(background_sprites, alligator, log1, log2, log3)
        all_sprites.add(background_sprites, alligator, log1, log2, log3, player)
#        sprites.add(player)
#        all_sprites.add(player)
=======
>>>>>>> 0aa13e0 (adding cave 4)

        all_sprites.add( alligator, log1, log2, log3, cave4,cave1,cave2,cave3, player)
=======
        all_sprites.update()
        new_level.kill()
        lake = Lake(-2, 255)  # Create the Lake and its position x, y
        lake_sprites.add(lake)  # Add lake
        all_sprites.add(background_sprites, alligator, log_sprites)

        all_sprites.add(alligators_sprites, cave1,cave2,cave3)
>>>>>>> a85e74e (Corrected logs / frogs - now working as intended)
=======

        new_level.kill()
        lake = Lake(-2, 255)  # Create the Lake and its position x, y
        lake_sprites.add(lake)  # Add lake
        cave1 = Caves(-90, -20, 'Images/minicave.png',420,420)
        cave2 = Caves(50, -20, 'Images/minicave.png',420,420)
        cave3 = Caves(170, -20, 'Images/minicave.png',420,420)
        cave4 = Caves(375, -55, 'Images/main cave.png',500, 320)
        cave_sprites = pygame.sprite.LayeredUpdates()
        cave_sprites.add(cave1, cave2, cave3, cave4)


        cave_frog1= CaveFrog(88,180)
        cave_frog2 = CaveFrog(217,180)
        cave_frog3= CaveFrog(345,180)
        cave_frog4 = CaveFrog(600,150)
        cave_frog_sprites = pygame.sprite.LayeredUpdates()
        

        all_sprites.add(alligators_sprites, log_sprites, cave_sprites, cave_frog_sprites, player_sprites)
>>>>>>> c7147e1 (Updated caves)

>>>>>>> 8c91984 (add caves, add collision detection frog/caves)
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py

        for car in cars.sprites():
            car.kill() # remove cars
        current_background = pygame.image.load('Images/bg1.png').convert()
        current_background = pygame.transform.scale(current_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py

        player.reset_player()
        
=======
<<<<<<< HEAD
<<<<<<< HEAD
        
=======
        player.reset_player()
        

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 35d6b74 (add sounds to different levels):car moving1.py
=======
=======
>>>>>>> eb25d32 (Updated caves)
<<<<<<< HEAD
=======
        player.reset_player()
        

>>>>>>> 0823d0d (adding leap_frog.py)
<<<<<<< HEAD
>>>>>>> 40ede70 (adding leap_frog.py)
=======
=======
        player.reset_player()

>>>>>>> c7147e1 (Updated caves)
>>>>>>> eb25d32 (Updated caves)
        mixer.music.stop()
        swamp_sound = mixer.music.load("Images/mixkit-insects-birds-and-frogs-in-the-swamp-ambience-40.wav")
        mixer.music.play()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD:leap_frog.py
=======
        
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
=======
>>>>>>> 33ff7ab (add sounds to different levels)
>>>>>>> 35d6b74 (add sounds to different levels):car moving1.py
=======
=======
>>>>>>> eb25d32 (Updated caves)
<<<<<<< HEAD
>>>>>>> 33ff7ab (add sounds to different levels)
=======
>>>>>>> 0823d0d (adding leap_frog.py)
<<<<<<< HEAD
>>>>>>> 40ede70 (adding leap_frog.py)
=======
=======

>>>>>>> 6ce169e (adding leap_frog.py)
<<<<<<< HEAD
>>>>>>> 2ccb3e7 (adding leap_frog.py)
=======
=======
>>>>>>> c7147e1 (Updated caves)
>>>>>>> eb25d32 (Updated caves)
        alligators = []
        num_alligators = 4

        for alligator in range(num_alligators):
            alligator = Gator(200, 400)
            alligators.append(alligator)
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py

            all_sprites.add(alligator)
<<<<<<< HEAD:leap_frog.py

    alligators_hit = pygame.sprite.spritecollide(player, alligators_sprites, False, pygame.sprite.collide_mask)
=======
=======
            sprites.add(alligator)
>>>>>>> 856efea (Removed logs from first screen.):car moving1.py
    
    alligators_hit = pygame.sprite.spritecollide(player, alligators_group, False, pygame.sprite.collide_mask)
   
>>>>>>> 1d9bfbf (Adding logs to new main code and backgrounds):car moving1.py
=======
#           sprites.add(alligator)
=======

>>>>>>> ce4576c (adding cave 4):car moving1.py
            all_sprites.add(alligator)

<<<<<<< HEAD
    
=======

>>>>>>> c7147e1 (Updated caves)
    alligators_hit = pygame.sprite.spritecollide(player, alligators_sprites, False, pygame.sprite.collide_mask)
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
    player_colliding_with_alligator = False

    for gator in alligators_hit:
        player.health -= 10
        if player.health == 0 and player.lives > 0:
            player.lives -= 1
            player.health = 100
        elif player.health == 0 and player.lives == 0:
            player.alive = False
            player_colliding_with_alligator = True

    if len(alligators_hit) == 0 or pygame.sprite.collide_mask(log, player):
        player_colliding_with_alligator = False

    # Check for collision between player and logs
    for log in log_sprites:
        if pygame.sprite.collide_mask(log, player):
            log.carry_player(player)

<<<<<<< HEAD:leap_frog.py
    # Check for collision between player and logs
<<<<<<< HEAD
    if current_level == 2:
        for log in log_sprites:
            if pygame.sprite.collide_mask(log, player):
                log.carry_player(player)
=======
    for log in log_sprites:
        if pygame.sprite.collide_mask(log, player):
            log.carry_player(player)
>>>>>>> 675536f (Adding more logs)

    if current_level == 2:

        lilypads = []
        num_lilypads = 4

<<<<<<< HEAD
        for lilypad in range(num_lilypads):
            lilypads = LilyPad(200, 400)
            lilypad_sprites.add(lilypads) 
        
=======

<<<<<<< HEAD

<<<<<<< HEAD


    #lilypads = []
    #num_lilypads = 4

    #for lilypad in range(num_lilypads):
        #lilypads = LilyPad(200, 400)
        #lilypads.append(lilypads)
        #all_sprites.add(lilypads)
>>>>>>> a875787 (saving changes):car moving1.py

    
<<<<<<< HEAD:leap_frog.py
    #check for collision between player and caves

    if current_level == 2 and pygame.sprite.collide_mask(player, cave1) :
        cave_frog_sprites.add(cave_frog1)
        player.reset_pos()
        cave_frog1.image.set_colorkey((0, 0, 0))

    elif current_level == 2 and pygame.sprite.collide_mask(player, cave2):
        cave_frog_sprites.add(cave_frog2)
=======
    # Check for collision between player and caves
    if pygame.sprite.collide_mask(player, cave1): 
=======
=======
=======
>>>>>>> 0aa13e0 (adding cave 4)
    #check for collision between player and caves
<<<<<<< HEAD:leap_frog.py
    if pygame.sprite.collide_mask(player, cave1): 
#       sprites.add(cave_frog1)
>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
       all_sprites.add(cave_frog1)
       player.reset_pos()
       cave_frog1.image.set_colorkey((0, 0, 0))  
  

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
    elif pygame.sprite.collide_mask(player, cave2): 
        all_sprites.add(cave_frog2)
>>>>>>> 675536f (Adding more logs)
        player.reset_pos()  # Reset the player's position
        cave_frog2.image.set_colorkey((0, 0, 0))

    elif current_level == 2 and pygame.sprite.collide_mask(player, cave3):
        cave_frog_sprites.add(cave_frog3)
        player.reset_pos()  # Reset the player's position
        cave_frog3.image.set_colorkey((0, 0, 0))

<<<<<<< HEAD
    elif current_level == 2 and pygame.sprite.collide_mask(player, cave4):
       cave_frog_sprites.add(cave_frog4)
       player.reset_pos()  # Reset the player's position
       cave_frog4.image.set_colorkey((0, 0, 0)) 
=======
    elif pygame.sprite.collide_mask(player, cave3):
        all_sprites.add(cave_frog3)
        player.reset_pos()  # Reset the player's position
        cave_frog3.image.set_colorkey((0, 0, 0)) 

>>>>>>> 675536f (Adding more logs)

    screen.blit(current_background, (scroll_x, scroll_y))

    lake_sprites.draw(screen)
<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
    
    cave_frog_sprites.draw(screen)
    cave_frog_sprites.update(screen)
    
=======
    player_sprites.draw(screen)
    logs_group.draw(screen)
    all_sprites.update()
>>>>>>> 1d9bfbf (Adding logs to new main code and backgrounds):car moving1.py
    all_sprites.draw(screen)
    lilypad_sprites.draw(screen)
    
    player_sprites.draw(screen)
    all_sprites.update()

    health_bar.update()
<<<<<<< HEAD:leap_frog.py

    cave_frog_sprites.draw(screen)
    cave_frog_sprites.update()
=======
    player.update()
    logs_group.update()
>>>>>>> 1d9bfbf (Adding logs to new main code and backgrounds):car moving1.py

=======
    sprites.update()
    sprites.draw(screen)
    health_bar.update()
    
>>>>>>> 856efea (Removed logs from first screen.):car moving1.py
=======
    elif pygame.sprite.collide_mask(player, log2): #colliding with logs for test purposes, it is supposed to be cave2
=======
    elif pygame.sprite.collide_mask(player, cave2): 
>>>>>>> 5167da6 (fix frog/cave collision):car moving1.py
#        sprites.add(cave_frog2)
        all_sprites.add(cave_frog2)
        player.reset_pos()  # Reset the player's position
        cave_frog2.image.set_colorkey((0, 0, 0)) 
=======
    if player.rect.colliderect(new_level.rect) and pygame.sprite.collide_mask(player, cave1) :
<<<<<<< HEAD
         

            all_sprites.add(cave_frog1)
            player.reset_pos()
            cave_frog1.image.set_colorkey((0, 0, 0))  
  

    elif player.rect.colliderect(new_level.rect) and pygame.sprite.collide_mask(player, cave2): 
>>>>>>> ce4576c (adding cave 4):car moving1.py

            all_sprites.add(cave_frog2)
            player.reset_pos()  # Reset the player's position
            cave_frog2.image.set_colorkey((0, 0, 0)) 

    elif player.rect.colliderect(new_level.rect) and pygame.sprite.collide_mask(player, cave3):

            all_sprites.add(cave_frog3)
            player.reset_pos()  # Reset the player's position
            cave_frog3.image.set_colorkey((0, 0, 0)) 
=======
        cave_frog_sprites.add(cave_frog1)
        player.reset_pos()
        cave_frog1.image.set_colorkey((0, 0, 0))

    elif player.rect.colliderect(new_level.rect) and pygame.sprite.collide_mask(player, cave2):
        cave_frog_sprites.add(cave_frog2)
        player.reset_pos()  # Reset the player's position
        cave_frog2.image.set_colorkey((0, 0, 0))

    elif player.rect.colliderect(new_level.rect) and pygame.sprite.collide_mask(player, cave3):
        cave_frog_sprites.add(cave_frog3)
        player.reset_pos()  # Reset the player's position
        cave_frog3.image.set_colorkey((0, 0, 0))
>>>>>>> c7147e1 (Updated caves)

    elif player.rect.colliderect(new_level.rect) and pygame.sprite.collide_mask(player, cave4):
       cave_frog_sprites.add(cave_frog4)
       player.reset_pos()  # Reset the player's position
       cave_frog4.image.set_colorkey((0, 0, 0)) 

<<<<<<< HEAD
>>>>>>> 8c91984 (add caves, add collision detection frog/caves)
=======
    
>>>>>>> 19cdcf2 (add the fourth cave)
    screen.blit(current_background, (scroll_x, scroll_y))


    lake_sprites.draw(screen)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    
    cave_fro_sprites.draw(screen)
    cave_fro_sprites.update(screen)
    
    all_sprites.draw(screen)

    all_sprites.update()

    all_sprites.draw(screen)
=======
=======
    cave_frog_sprites.draw(screen)
    cave_frog_sprites.update(screen)
>>>>>>> 0823d0d (adding leap_frog.py)
    all_sprites.draw(screen)
    player_sprites.draw(screen)
    all_sprites.update()
>>>>>>> a85e74e (Corrected logs / frogs - now working as intended)
=======
    all_sprites.draw(screen)
    player_sprites.draw(screen)
    all_sprites.update()
>>>>>>> c7147e1 (Updated caves)

    health_bar.update()
<<<<<<< HEAD
<<<<<<< HEAD
=======

    cave_frog_sprites.draw(screen)
    cave_frog_sprites.update()

    pygame.display.flip()
    clock.tick(60)
>>>>>>> 6ce169e (adding leap_frog.py)

<<<<<<< HEAD
<<<<<<< HEAD:leap_frog.py

>>>>>>> deb5e7c (add caves, add collision detection frog/caves):car moving1.py
=======
=======
<<<<<<< HEAD
>>>>>>> eb25d32 (Updated caves)
 #   cave_sprites.update()
<<<<<<< HEAD
>>>>>>> b885374 (add the fourth cave):car moving1.py
=======
=======
 
>>>>>>> 0823d0d (adding leap_frog.py)
>>>>>>> 40ede70 (adding leap_frog.py)
    pygame.display.flip()
<<<<<<< HEAD
    clock.tick(60)
<<<<<<< HEAD

<<<<<<< HEAD:leap_frog.py
<<<<<<< HEAD:leap_frog.py
mixer.music.stop()

pygame.quit()
sys.exit()

=======
>>>>>>> ce4576c (adding cave 4):car moving1.py
=======
=======
>>>>>>> 2b4e666 (add new sound)
<<<<<<< HEAD:leap_frog.py
>>>>>>> 9bcd7ea (add new sound):car moving1.py
=======
=======
    clock.tick(60)
>>>>>>> 8a35226 (deleted empty line)
<<<<<<< HEAD
>>>>>>> 4b6ba23 (deleted empty line):car moving1.py
=======
=======
pygame.quit()
sys.exit()
>>>>>>> c7147e1 (Updated caves)
>>>>>>> eb25d32 (Updated caves)
