import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Editor")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load image
try:
    image = pygame.image.load("resources/in.jpg")
    image = pygame.transform.scale(image, (width, height))
except FileNotFoundError:
    try:
        image = pygame.image.load("resources/in.png")
        image = pygame.transform.scale(image, (width, height))
    except FileNotFoundError:
        image = pygame.image.load("resources/in.jpeg")
        image = pygame.transform.scale(image, (width, height))   


# Create a surface for drawing
drawing_surface = pygame.Surface((width, height), pygame.SRCALPHA)

# Set up drawing variables
drawing = False
brush_size = 10
brush_color = black
eraser_mode = False

# Define color buttons
button_size = 30
button_outline_width = 2  # Width of the outline
color_buttons = [
    pygame.Rect(10, 10, button_size, button_size),
    pygame.Rect(50, 10, button_size, button_size),
    pygame.Rect(90, 10, button_size, button_size)
]

# Color options
color_options = [white, black, (255, 0, 0)]  # You can add more colors as needed

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(screen, "export/out.jpg")
            pygame.quit()
            sys.exit()

        # Handle mouse events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
            elif event.button == 4:  # Scroll Up
                brush_size += 1
            elif event.button == 5:  # Scroll Down
                brush_size = max(1, brush_size - 1)
            elif event.button == 3:  # Right mouse button for eraser toggle
                eraser_mode = not eraser_mode

            # Check if a color button is clicked
            for i, button in enumerate(color_buttons):
                if button.collidepoint(event.pos):
                    brush_color = color_options[i]

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

        # Handle drawing
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if eraser_mode:
                    # Create a transparent circle for erasing
                    erase_circle = pygame.Surface((brush_size, brush_size), pygame.SRCALPHA)
                    pygame.draw.circle(erase_circle, white, (brush_size // 2, brush_size // 2), brush_size // 2)
                    # Blit the transparent circle onto the drawing surface
                    drawing_surface.blit(erase_circle, (event.pos[0] - brush_size // 2, event.pos[1] - brush_size // 2))
                else:
                    pygame.draw.circle(drawing_surface, brush_color, event.pos, brush_size)

    # Update display
    screen.blit(image, (0, 0))
    screen.blit(drawing_surface, (0, 0))

    # Draw color buttons with an outline
    for i, button in enumerate(color_buttons):
        pygame.draw.rect(screen, color_options[i], button)
        pygame.draw.rect(screen, black, button, button_outline_width)  # Draw outline

    # Draw brush indicator
    if True:
        pygame.draw.circle(screen, brush_color, pygame.mouse.get_pos(), brush_size )
        pygame.draw.circle(screen, brush_color, pygame.mouse.get_pos(), brush_size )

    pygame.display.flip()
