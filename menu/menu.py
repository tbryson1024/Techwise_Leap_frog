import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu Screen")

# Define colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Function to draw the menu with the buttons
def draw_menu():
    screen.fill(GREEN)  # Fill the screen with green color
    # change to correct path for font
    font = pygame.font.Font('/home/tbryson/techwiseTheirs/Techwise_Leap_frog/menu/Lilita_One.ttf', 36)
    text = font.render("Frogger", True, BLACK)  # Black text
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 200))

    # Draw the start button
    start_button_width, start_button_height = 200, 50
    start_button_x = screen_width // 2 - start_button_width // 2
    start_button_y = 300
    pygame.draw.rect(screen, BLACK, (start_button_x, start_button_y, start_button_width, start_button_height))
    start_text = font.render("Start", True, GREEN)
    screen.blit(start_text, (start_button_x + start_button_width // 2 - start_text.get_width() // 2, start_button_y + start_button_height // 2 - start_text.get_height() // 2))

    # Draw the quit button
    quit_button_width, quit_button_height = 200, 50
    quit_button_x = screen_width // 2 - quit_button_width // 2
    quit_button_y = 400
    pygame.draw.rect(screen, BLACK, (quit_button_x, quit_button_y, quit_button_width, quit_button_height))
    quit_text = font.render("Quit", True, GREEN)
    screen.blit(quit_text, (quit_button_x + quit_button_width // 2 - quit_text.get_width() // 2, quit_button_y + quit_button_height // 2 - quit_text.get_height() // 2))

    pygame.display.flip()  # Update the display

# Function to draw the gameplay screen
def draw_gameplay_screen():
    screen.fill(BLACK)  # Fill the screen with black color
    pygame.display.flip()  # Update the display

# Function to handle button click events
def handle_button_click(mouse_pos):
    start_button_x, start_button_y, start_button_width, start_button_height = screen_width // 2 - 100, 300, 200, 50
    quit_button_x, quit_button_y, quit_button_width, quit_button_height = screen_width // 2 - 100, 400, 200, 50

    if start_button_x <= mouse_pos[0] <= start_button_x + start_button_width and start_button_y <= mouse_pos[1] <= start_button_y + start_button_height:
        print("Start button clicked!")
        # switch to the gameplay screen
        run_gameplay_screen()
    elif quit_button_x <= mouse_pos[0] <= quit_button_x + quit_button_width and quit_button_y <= mouse_pos[1] <= quit_button_y + quit_button_height:
        pygame.quit()
        quit()

# Function to run the gameplay screen
def run_gameplay_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_gameplay_screen()

        pygame.display.flip()  # Update the display

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    handle_button_click(pygame.mouse.get_pos())

        draw_menu()

        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__ == "__main__":
    main()
