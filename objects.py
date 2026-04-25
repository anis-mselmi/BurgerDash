import pygame
import random


class Button:
    def __init__(self, image: pygame.Surface, rect: pygame.Rect, item_name: str):
        self.image = image
        self.rect = rect
        self.item_name = item_name
        self.hovered = False

    def draw(self, screen: pygame.Surface):
        if self.hovered:
            border_rect = self.rect.inflate(8, 8)
            pygame.draw.rect(screen, (255, 220, 0), border_rect, border_radius=12)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=10)
        screen.blit(self.image, self.rect)

    def check_hover(self, mouse_pos: tuple):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos: tuple) -> bool:
        return self.rect.collidepoint(mouse_pos)


class Customer:
    def __init__(self, image: pygame.Surface, x: int, y: int):
        self.image = pygame.transform.scale(image, (120, 180))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)


class Order:
    ITEMS = ["burger", "fries", "drink"]

    def __init__(self, images: dict):
        self.images = images
        self.current = None
        self.image = None
        self.new_order()

    def new_order(self):
        self.current = random.choice(self.ITEMS)
        raw_img = self.images[self.current]
        self.image = pygame.transform.scale(raw_img, (100, 100))

    def draw(self, screen: pygame.Surface, x: int, y: int):
        bubble_rect = pygame.Rect(x - 10, y - 10, 120, 120)
        pygame.draw.rect(screen, (255, 255, 255), bubble_rect, border_radius=15)
        pygame.draw.rect(screen, (220, 50, 50), bubble_rect, width=3, border_radius=15)
        screen.blit(self.image, (x, y))
