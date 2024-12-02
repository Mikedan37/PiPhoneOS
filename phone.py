import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1020, 600  # Wider screen for horizontal layout
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the Pygame window
pygame.display.set_caption("Phone Keypad")  # Set the window title
font = pygame.font.Font(None, 40)  # Smaller font for numbers
small_font = pygame.font.Font(None, 25)  # Smaller font for subtext (alphabets below numbers)

# Colors (RGB format)
BLACK = (0, 0, 0)  # Background color
WHITE = (255, 255, 255)  # Circle background color
GREY = (70, 70, 70)  # Button color

# Load the new PNG file for the phone logo
new_phone_logo = pygame.image.load("/Users/manas/Documents/Pi_Phone/PIPHONE IMAGES/iphone.png")  # Replace with the path to your PNG
logo_size = 35  # Adjusted size of the phone logo to fit properly
new_phone_logo = pygame.transform.scale(new_phone_logo, (logo_size, logo_size))  # Resize the logo

# Button configurations
button_radius = 35  # Reduced circle radius for all buttons
button_spacing = 20  # Reduced spacing between buttons for clarity
keypad_width = 3 * (button_radius * 2 + button_spacing)  # Total width of the keypad grid
keypad_height = 4 * (button_radius * 2 + button_spacing)  # Total height of the keypad grid

# Centering offsets
start_x = (WIDTH - keypad_width) // 2  # Starting x position to center the keypad
start_y = (HEIGHT - keypad_height) // 2  # Starting y position to center the keypad

# Button positions and labels
buttons = [
    {"pos": (start_x + button_spacing + button_radius, start_y + button_spacing + button_radius), "text": "1"},
    {"pos": (start_x + button_spacing * 2 + button_radius * 3, start_y + button_spacing + button_radius), "text": "2", "subtext": "ABC"},
    {"pos": (start_x + button_spacing * 3 + button_radius * 5, start_y + button_spacing + button_radius), "text": "3", "subtext": "DEF"},
    {"pos": (start_x + button_spacing + button_radius, start_y + button_spacing * 2 + button_radius * 3), "text": "4", "subtext": "GHI"},
    {"pos": (start_x + button_spacing * 2 + button_radius * 3, start_y + button_spacing * 2 + button_radius * 3), "text": "5", "subtext": "JKL"},
    {"pos": (start_x + button_spacing * 3 + button_radius * 5, start_y + button_spacing * 2 + button_radius * 3), "text": "6", "subtext": "MNO"},
    {"pos": (start_x + button_spacing + button_radius, start_y + button_spacing * 3 + button_radius * 5), "text": "7", "subtext": "PQRS"},
    {"pos": (start_x + button_spacing * 2 + button_radius * 3, start_y + button_spacing * 3 + button_radius * 5), "text": "8", "subtext": "TUV"},
    {"pos": (start_x + button_spacing * 3 + button_radius * 5, start_y + button_spacing * 3 + button_radius * 5), "text": "9", "subtext": "WXYZ"},
    {"pos": (start_x + button_spacing + button_radius, start_y + button_spacing * 4 + button_radius * 7), "text": "*"},
    {"pos": (start_x + button_spacing * 2 + button_radius * 3, start_y + button_spacing * 4 + button_radius * 7), "text": "0"},
    {"pos": (start_x + button_spacing * 3 + button_radius * 5, start_y + button_spacing * 4 + button_radius * 7), "text": "#"},
]

# Call button position
call_button = {
    "pos": (start_x + keypad_width // 2, start_y + keypad_height + button_spacing * 2)
}

# Text to display
dialed_number = ""  # Variable to store the phone number being entered by the user

# Function to draw the keypad
def draw_keypad():
    """
    This function is responsible for rendering the entire keypad and dialed number on the screen.
    """
    screen.fill(BLACK)  # Fill the screen with the background color

    # Loop through each button in the "buttons" list and render them
    for button in buttons:
        # Draw a circle for each button
        pygame.draw.circle(screen, GREY, button["pos"], button_radius)  # Buttons with a smaller radius

        # Render the number (main text)
        text = font.render(button["text"], True, WHITE)  # Render the number in white
        screen.blit(text, (button["pos"][0] - text.get_width() // 2, button["pos"][1] - 15))  # Center text and move it up

        # Render the subtext (alphabets) if present
        if "subtext" in button:  # Check if the button has subtext
            subtext = small_font.render(button["subtext"], True, WHITE)  # Render the subtext
            # Position the subtext slightly below the number
            screen.blit(subtext, (button["pos"][0] - subtext.get_width() // 2, button["pos"][1] + 10))

    # Draw the call button as a white circle with the new logo inside
    pygame.draw.circle(screen, WHITE, call_button["pos"], button_radius)  # Draw the circular background
    screen.blit(new_phone_logo, (call_button["pos"][0] - new_phone_logo.get_width() // 2, call_button["pos"][1] - new_phone_logo.get_height() // 2))  # Center the new logo inside the circle

    # Draw the dialed number at the top of the screen
    number_text = font.render(dialed_number, True, WHITE)  # Render the dialed number
    screen.blit(number_text, (WIDTH // 2 - number_text.get_width() // 2, 20))  # Display at the top, centered

# Main loop
running = True  # Variable to keep the game running
while running:
    for event in pygame.event.get():  # Process all events in the event queue
        if event.type == pygame.QUIT:  # Check if the user wants to close the window
            running = False  # Exit the loop, ending the game
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check if the user clicks the mouse
            mouse_pos = pygame.mouse.get_pos()  # Get the current position of the mouse click
            for button in buttons:  # Loop through all the buttons to check if one is clicked
                # Check if the mouse click is inside the current button's circle
                if (mouse_pos[0] - button["pos"][0]) ** 2 + (mouse_pos[1] - button["pos"][1]) ** 2 <= button_radius ** 2:
                    dialed_number += button["text"]  # Append the button's number to the dialed number
                    break
            # Check if the call button is clicked
            if (call_button["pos"][0] - button_radius <= mouse_pos[0] <= call_button["pos"][0] + button_radius and
                call_button["pos"][1] - button_radius <= mouse_pos[1] <= call_button["pos"][1] + button_radius):
                print(f"Calling {dialed_number}...")  # Simulate a call by printing the dialed number
                dialed_number = ""  # Clear the dialed number after the call

    # Draw everything on the screen
    draw_keypad()

    # Update the display with the new frame
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()  # Exit the program
