# Game objects for BurgerDash
import pygame
import random


class Button:
    def __init__(self, image, rect, item_name):
        self.image = image
        self.rect = rect
        self.item_name = item_name
        self.hovered = False

    def draw(self, screen):
        if self.hovered:
            pygame.draw.rect(screen, (255, 220, 0), self.rect.inflate(8, 8), border_radius=12)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=10)
        screen.blit(self.image, self.rect)

    def check_hover(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


class Customer:
    def __init__(self, image, x, y):
        self.image = pygame.transform.scale(image, (120, 180))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Order:
    ITEMS = ["burger", "fries", "drink"]

    def __init__(self, images):
        self.images = images
        self.current = None
        self.image = None
        self.new_order()

    def new_order(self):
        self.current = random.choice(self.ITEMS)
        self.image = pygame.transform.scale(self.images[self.current], (100, 100))

    def draw(self, screen, x, y):
        bubble = pygame.Rect(x - 10, y - 10, 120, 120)
        pygame.draw.rect(screen, (255, 255, 255), bubble, border_radius=15)
        pygame.draw.rect(screen, (220, 50, 50), bubble, width=3, border_radius=15)
        screen.blit(self.image, (x, y))
