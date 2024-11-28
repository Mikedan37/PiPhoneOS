import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Phone Keypad")
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 35)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
GREEN = (0, 255, 0)

# Button positions and labels
buttons = [
    {"pos": (100, 150), "text": "1"},
    {"pos": (200, 150), "text": "2", "subtext": "ABC"},
    {"pos": (300, 150), "text": "3", "subtext": "DEF"},
    {"pos": (100, 250), "text": "4", "subtext": "GHI"},
    {"pos": (200, 250), "text": "5", "subtext": "JKL"},
    {"pos": (300, 250), "text": "6", "subtext": "MNO"},
    {"pos": (100, 350), "text": "7", "subtext": "PQRS"},
    {"pos": (200, 350), "text": "8", "subtext": "TUV"},
    {"pos": (300, 350), "text": "9", "subtext": "WXYZ"},
    {"pos": (100, 450), "text": "*"},
    {"pos": (200, 450), "text": "0"},
    {"pos": (300, 450), "text": "#"},
]

# Green call button
call_button = {"pos": (200, 550), "radius": 40, "color": GREEN, "text": ""}

# Text to display
dialed_number = ""

# Function to draw the keypad
def draw_keypad():
    screen.fill(BLACK)

    # Draw buttons
    for button in buttons:
        pygame.draw.circle(screen, GREY, button["pos"], 40)
        text = font.render(button["text"], True, WHITE)
        screen.blit(text, (button["pos"][0] - text.get_width() // 2, button["pos"][1] - 20))
        if "subtext" in button:
            subtext = small_font.render(button["subtext"], True, WHITE)
            screen.blit(subtext, (button["pos"][0] - subtext.get_width() // 2, button["pos"][1] + 10))

    # Draw call button
    pygame.draw.circle(screen, call_button["color"], call_button["pos"], call_button["radius"])
    pygame.draw.polygon(screen, BLACK, [(180, 540), (220, 540), (200, 560)])

    # Draw dialed number
    number_text = font.render(dialed_number, True, WHITE)
    screen.blit(number_text, (WIDTH // 2 - number_text.get_width() // 2, 50))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                # Check if button is clicked
                if (mouse_pos[0] - button["pos"][0]) ** 2 + (mouse_pos[1] - button["pos"][1]) ** 2 <= 40 ** 2:
                    dialed_number += button["text"]
                    break
            # Check if call button is clicked
            if (mouse_pos[0] - call_button["pos"][0]) ** 2 + (mouse_pos[1] - call_button["pos"][1]) ** 2 <= call_button["radius"] ** 2:
                print(f"Calling {dialed_number}...")
                dialed_number = ""  # Clear after "calling"

    # Draw everything
    draw_keypad()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
