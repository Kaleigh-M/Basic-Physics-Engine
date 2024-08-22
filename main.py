import pygame
import sys
import random
import pygame_gui

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.1  # Gravity acceleration (reduced)
BOUNCE_FACTOR = 0.9  # Bounce factor (increased)

GREY = (255, 255, 255)
PARTICLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Particle class
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, shape, size, color):
        super().__init__()
        self.shape = shape
        if self.shape == "circle":
            self.image = pygame.Surface((2 * size, 2 * size), pygame.SRCALPHA)
            pygame.draw.circle(self.image, color, (size, size), size)
        elif self.shape == "rectangle":
            self.image = pygame.Surface((2 * size, 2 * size), pygame.SRCALPHA)
            pygame.draw.rect(self.image, color, (0, 0, 2 * size, 2 * size))
        elif self.shape == "triangle":
            self.image = pygame.Surface((2 * size, 2 * size), pygame.SRCALPHA)
            pygame.draw.polygon(self.image, color, [(0, 2 * size), (size, 0), (2 * size, 2 * size)])
        self.rect = self.image.get_rect(center=(x, y))
        self.size = size
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]

    def update(self):
        self.velocity[1] += GRAVITY  # Gravity effect
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Bounce off walls
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocity[0] = -self.velocity[0] * BOUNCE_FACTOR

        # Bounce off ground
        if self.shape == "circle" and self.rect.bottom > HEIGHT:
            self.velocity[1] = -self.velocity[1] * BOUNCE_FACTOR

        # Prevent particles from going into each other
        for particle in all_sprites:
            if particle != self:
                if self.shape == "circle" and pygame.sprite.collide_circle(self, particle):
                    self.velocity[0] = -self.velocity[0] * BOUNCE_FACTOR
                    self.velocity[1] = -self.velocity[1] * BOUNCE_FACTOR
                elif self.shape == "rectangle" and self.rect.colliderect(particle.rect):
                    self.velocity[0] = 0
                    self.velocity[1] = 0
                elif self.shape == "triangle" and pygame.sprite.collide_rect(self, particle):
                    self.velocity[0] = 0 
                    self.velocity[1] = 0

        # Prevent particles from falling off the bottom
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine with Grab and Gravity")

all_sprites = pygame.sprite.Group()

gui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to add a particle of the specified shape
def add_particle(shape):
    color = random.choice(PARTICLE_COLORS)
    size = random.randint(20, 40)
    if shape == "circle":
        particle = Particle(random.randint(size, WIDTH - size), random.randint(size, HEIGHT - size), shape, size, color)
    elif shape == "rectangle":
        particle = Particle(random.randint(size, WIDTH - size), random.randint(size, HEIGHT - size), shape, size, color)
    elif shape == "triangle":
        particle = Particle(random.randint(size, WIDTH - size), random.randint(size, HEIGHT - size), shape, size, color)
    all_sprites.add(particle)

add_circle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (100, 30)), text='Add Circle', manager=gui_manager)
add_rectangle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((120, 10), (120, 30)), text='Add Rectangle', manager=gui_manager)
add_triangle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 10), (120, 30)), text='Add Triangle', manager=gui_manager)
remove_all_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((380, 10), (120, 30)), text='Remove All', manager=gui_manager)

# Main game loop
running = True
grabbed_particle = None  # Reference to the currently grabbed particle
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
        
            for particle in all_sprites:
                if particle.rect.collidepoint(event.pos):
                    grabbed_particle = particle
        elif event.type == pygame.MOUSEBUTTONUP:
            grabbed_particle = None

        # Handle GUI events
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == add_circle_button:
                    add_particle("circle")
                elif event.ui_element == add_rectangle_button:
                    add_particle("rectangle")
                elif event.ui_element == add_triangle_button:
                    add_particle("triangle")
                elif event.ui_element == remove_all_button:
                    all_sprites.empty()

        # Pass events to GUI manager
        gui_manager.process_events(event)

    # If a particle is grabbed, move it with the mouse
    if grabbed_particle:
        grabbed_particle.rect.center = pygame.mouse.get_pos()

    all_sprites.update()

    screen.fill(GREY)
    all_sprites.draw(screen)

    gui_manager.draw_ui(screen)

    pygame.display.flip()

    clock.tick(FPS)

    gui_manager.update(FPS)

pygame.quit()
sys.exit()
