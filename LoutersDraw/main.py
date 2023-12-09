import pygame
import sys
import os
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("LoutersDraw V1.1")

white = (255, 255, 255)
black = (0, 0, 0)

try:
    image = pygame.image.load("import/in.jpg")
    image = pygame.transform.scale(image, (width, height))
except FileNotFoundError:
    try:
        image = pygame.image.load("import/in.png")
        image = pygame.transform.scale(image, (width, height))
    except FileNotFoundError:
        try:
            image = pygame.image.load("import/in.jpeg")
            image = pygame.transform.scale(image, (width, height))   
        except FileNotFoundError:
            os.rename("resources/cav.rgif", "resources/tmp.jpg")
            image = pygame.image.load("resources/tmp.jpg")
            image = pygame.transform.scale(image, (width,height))
            os.rename("resources/tmp.jpg", "resources/cav.rgif")




drawing_surface = pygame.Surface((width, height), pygame.SRCALPHA)
clock = pygame.time.Clock()
drawing = False
brush_size = 10
brush_color = black
eraser_mode = False

button_size = 30
button_outline_width = 2 
color_buttons = [
    pygame.Rect(10, 10, button_size, button_size),
    pygame.Rect(50, 10, button_size, button_size),
    pygame.Rect(90, 10, button_size, button_size)
]

color_options = [white, black, (255, 0, 0)] 

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
            elif event.button == 3:  # Right mouse button 
                eraser_mode = not eraser_mode

            # Check if color button is clicked
            for i, button in enumerate(color_buttons):
                if button.collidepoint(event.pos):
                    brush_color = color_options[i]

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

        # drawing
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if eraser_mode:
                    erase_circle = pygame.Surface((brush_size, brush_size), pygame.SRCALPHA)
                    pygame.draw.circle(erase_circle, white, (brush_size // 2, brush_size // 2), brush_size // 2)
                    drawing_surface.blit(erase_circle, (event.pos[0] - brush_size // 2, event.pos[1] - brush_size // 2))
                else:
                    pygame.draw.circle(drawing_surface, brush_color, event.pos, brush_size)

    screen.blit(image, (0, 0))
    screen.blit(drawing_surface, (0, 0))

    for i, button in enumerate(color_buttons):
        pygame.draw.rect(screen, color_options[i], button)
        pygame.draw.rect(screen, black, button, button_outline_width)  # Draw outline

    if True:
        pygame.draw.circle(screen, brush_color, pygame.mouse.get_pos(), brush_size )
        

    pygame.display.flip()
    clock.tick(128)
