import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1024, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mobile OS with Icons")

# Colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (33, 33, 31)
DARK_GRAY = (169, 169, 169)
BLUE = (0, 122, 255)
DARK_BLUE = (0, 102, 204)
BLACK = (0, 0, 0)
SHADOW = (200, 200, 200)

# Font
font = pygame.font.Font(None, 36)

# Rounded Rectangle Button Class with Icon
class IconButton:
    def __init__(self, x, y, width, height, color, shadow_color, text, text_color, animation_color, icon_path, radius=15):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.shadow_color = shadow_color
        self.text = text
        self.text_color = text_color
        self.animation_color = animation_color
        self.radius = radius
        self.icon = pygame.image.load(icon_path)
        self.icon = pygame.transform.scale(self.icon, (height - 40, height - 40))  # Scale icon to fit button
        self.is_pressed = False

    def draw(self, surface):
        # Draw shadow
        shadow_rect = self.rect.move(5, 5)
        pygame.draw.rect(surface, self.shadow_color, shadow_rect, border_radius=self.radius)
        # Draw main button
        color = self.animation_color if self.is_pressed else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=self.radius)
        # Add text
        text_surface = font.render(self.text, True, self.text_color)
        surface.blit(
            text_surface,
            (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
             self.rect.y + self.rect.height - 30)
        )
        # Add icon
        surface.blit(
            self.icon,
            (self.rect.x + (self.rect.width - self.icon.get_width()) // 2,
             self.rect.y + 10)
        )

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

#Rounded Bottom KEYMenu
class KEYMenu:
    def __init__(self):
        # Dock buttons
        self.dock_buttons = [
            IconButton(60, 410, 120, 150, BLUE, SHADOW, "Phone", WHITE, DARK_BLUE, "PIPHONE IMAGES/Phone.png"),
            IconButton(250, 410, 120, 150, DARK_GRAY, SHADOW, "Messages", WHITE, BLACK, "PIPHONE IMAGES/Messages.png"),
            IconButton(440, 410, 120, 150,DARK_GRAY, SHADOW, "Settings", WHITE, BLACK,  "PIPHONE IMAGES/Settings.png"),
            IconButton(620, 410, 120, 150, DARK_GRAY, SHADOW, "Settings", WHITE, BLACK, "PIPHONE IMAGES/Files.png"),
            IconButton(800, 410, 120, 150, DARK_GRAY, SHADOW, "Settings", WHITE, BLACK, "PIPHONE IMAGES/Clock.png"),
        ]
        # Power button
        self.power_button = IconButton(920, 20, 80, 80, DARK_GRAY, SHADOW, "Exit", WHITE, BLACK,
                                       "PIPHONE IMAGES/Exit.png")

    def draw(self, surface):
        # Draw the dock background
        pygame.draw.rect(surface, BLACK, (30, 590, WIDTH - 100, -200), border_radius=50)

        # Draw dock buttons
        for button in self.dock_buttons:
            button.draw(surface)

        # Draw the power button
        self.power_button.draw(surface)

    def handle_click(self, pos):
        # Check dock buttons
        for button in self.dock_buttons:
            if button.is_clicked(pos):
                return button.text  # Return the text of the clicked button (e.g., "Phone")
        # Check power button
        if self.power_button.is_clicked(pos):
            return "Exit"
        return None

# Home Screen
def home_screen():
    key_menu = KEYMenu()  # Initialize the dock menu
    # Load the background image once
    backgroundIMG = pygame.image.load("PIPHONE IMAGES/BackgroundImage.png")
    backgroundIMG = pygame.transform.scale(backgroundIMG, (WIDTH, HEIGHT))  # Scale to screen size if necessary
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_button = key_menu.handle_click(event.pos)
                if clicked_button == "Phone":
                    phone_screen()
                elif clicked_button == "Messages":
                    messages_screen()
                elif clicked_button == "Exit":
                    pygame.quit()
                    sys.exit()

        # Draw the home screen
        #screen.fill(LIGHT_GRAY)

        # Draw the background image
        screen.blit(backgroundIMG, (0, 0))  # Position the background at (0, 0)

        key_menu.draw(screen)  # Draw the dock with its buttons and the power button

        pygame.display.flip()


# Phone Screen
def phone_screen():
    back_button = IconButton(412, 500, 200, 80, BLUE, SHADOW, "Back", WHITE, DARK_BLUE, "PIPHONE IMAGES/Exit.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    back_button.is_pressed = True

            if event.type == pygame.MOUSEBUTTONUP:
                if back_button.is_pressed and back_button.is_clicked(event.pos):
                    back_button.is_pressed = False
                    return  # Go back to the home screen

        # Draw the phone screen
        screen.fill(WHITE)
        back_button.draw(screen)

        pygame.display.flip()


# Messages Screen
def messages_screen():
    back_button = IconButton(412, 500, 200, 80, BLUE, SHADOW, "Back", WHITE, DARK_BLUE, "PIPHONE IMAGES/Exit.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    back_button.is_pressed = True

            if event.type == pygame.MOUSEBUTTONUP:
                if back_button.is_pressed and back_button.is_clicked(event.pos):
                    back_button.is_pressed = False
                    return  # Go back to the home screen

        # Draw the messages screen
        screen.fill(WHITE)
        back_button.draw(screen)

        pygame.display.flip()


# Start the app
if __name__ == "__main__":
    home_screen()