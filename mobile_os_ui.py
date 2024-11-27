import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1024, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mobile OS")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Button class
class Button:
    def __init__(self, x, y, width, height, color, text, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = font.render(self.text, True, self.text_color)
        surface.blit(
            text_surface,
            (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
             self.rect.y + (self.rect.height - text_surface.get_height()) // 2)
        )

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Home Screen
def home_screen():
    button_settings = Button(400, 200, 200, 100, GREEN, "Settings", WHITE)
    button_exit = Button(400, 350, 200, 100, RED, "Exit", WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_settings.is_clicked(event.pos):
                    settings_screen()
                if button_exit.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()

        # Draw the home screen
        screen.fill(WHITE)
        button_settings.draw(screen)
        button_exit.draw(screen)

        pygame.display.flip()

# Settings Screen
def settings_screen():
    back_button = Button(400, 500, 200, 100, BLUE, "Back", WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    return  # Go back to the home screen

        # Draw the settings screen
        screen.fill(BLACK)
        back_button.draw(screen)

        pygame.display.flip()

# Start the app
if __name__ == "__main__":
    home_screen()
