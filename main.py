import sys
import pygame
from objects import Button, Customer, Order

SCREEN_W = 800
SCREEN_H = 600
FPS = 60
ORDER_TIME = 5

WHITE  = (255, 255, 255)
RED    = (200, 30, 30)
YELLOW = (255, 210, 0)


def load_image(path, size=None):
    img = pygame.image.load(path).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    return img


def draw_text(screen, text, font, color, x, y, center=False):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(surface, rect)


def draw_panel(screen, rect, color=(0, 0, 0), alpha=160, radius=12):
    panel = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(panel, (*color, alpha), panel.get_rect(), border_radius=radius)
    screen.blit(panel, rect.topleft)


def draw_start_screen(screen, bg, font_title, font_sub):
    screen.blit(bg, (0, 0))
    draw_panel(screen, pygame.Rect(150, 160, 500, 280), (20, 20, 20), 180, 20)
    draw_text(screen, "BurgerDash", font_title, YELLOW, SCREEN_W // 2, 230, center=True)
    draw_text(screen, "Serve the right food before time runs out!", font_sub, WHITE, SCREEN_W // 2, 300, center=True)
    draw_text(screen, "Click the matching food item", font_sub, (200, 200, 200), SCREEN_W // 2, 335, center=True)
    btn = pygame.Rect(SCREEN_W // 2 - 100, 380, 200, 50)
    pygame.draw.rect(screen, RED, btn, border_radius=10)
    pygame.draw.rect(screen, YELLOW, btn, width=3, border_radius=10)
    draw_text(screen, "START GAME", font_sub, YELLOW, SCREEN_W // 2, 405, center=True)
    return btn


def draw_gameover_screen(screen, bg, font_title, font_sub, score, reason):
    screen.blit(bg, (0, 0))
    draw_panel(screen, pygame.Rect(150, 150, 500, 320), (20, 20, 20), 190, 20)
    draw_text(screen, "GAME OVER", font_title, RED, SCREEN_W // 2, 210, center=True)
    draw_text(screen, reason, font_sub, (255, 180, 180), SCREEN_W // 2, 275, center=True)
    draw_text(screen, f"Final Score: {score}", font_sub, YELLOW, SCREEN_W // 2, 315, center=True)
    btn = pygame.Rect(SCREEN_W // 2 - 100, 380, 200, 50)
    pygame.draw.rect(screen, RED, btn, border_radius=10)
    pygame.draw.rect(screen, YELLOW, btn, width=3, border_radius=10)
    draw_text(screen, "PLAY AGAIN", font_sub, YELLOW, SCREEN_W // 2, 405, center=True)
    return btn


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("BurgerDash — Fast Food Restaurant")
    clock = pygame.time.Clock()

    font_title = pygame.font.SysFont("Arial", 52, bold=True)
    font_sub   = pygame.font.SysFont("Arial", 26)
    font_ui    = pygame.font.SysFont("Arial", 22, bold=True)

    bg = load_image("assets/background.png", (SCREEN_W, SCREEN_H))

    food_imgs = {
        "burger": load_image("assets/burger.png",  (110, 110)),
        "fries":  load_image("assets/fries.png",   (110, 110)),
        "drink":  load_image("assets/drink.png",   (110, 110)),
    }

    customer = Customer(load_image("assets/customer.png"), 60, 260)
    order    = Order(food_imgs)

    btn_y   = SCREEN_H - 145
    start_x = SCREEN_W // 2 - 160
    buttons = [
        Button(food_imgs["burger"], pygame.Rect(start_x,       btn_y, 110, 110), "burger"),
        Button(food_imgs["fries"],  pygame.Rect(start_x + 160, btn_y, 110, 110), "fries"),
        Button(food_imgs["drink"],  pygame.Rect(start_x + 320, btn_y, 110, 110), "drink"),
    ]

    state     = "start"
    score     = 0
    timer     = ORDER_TIME
    reason    = ""
    last_time = pygame.time.get_ticks()

    while True:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if state == "start":
                    start_btn = draw_start_screen(screen, bg, font_title, font_sub)
                    if start_btn.collidepoint(mouse_pos):
                        state = "play"
                        score = 0
                        timer = ORDER_TIME
                        order.new_order()
                        last_time = pygame.time.get_ticks()

                elif state == "gameover":
                    retry_btn = draw_gameover_screen(screen, bg, font_title, font_sub, score, reason)
                    if retry_btn.collidepoint(mouse_pos):
                        state = "play"
                        score = 0
                        timer = ORDER_TIME
                        order.new_order()
                        last_time = pygame.time.get_ticks()

                elif state == "play":
                    for btn in buttons:
                        if btn.is_clicked(mouse_pos):
                            if btn.item_name == order.current:
                                score += 1
                                order.new_order()
                                timer = ORDER_TIME
                                last_time = pygame.time.get_ticks()
                            else:
                                reason = f"Wrong item! You served {btn.item_name}."
                                state = "gameover"

        if state == "play":
            elapsed = (pygame.time.get_ticks() - last_time) / 1000.0
            timer = max(0.0, ORDER_TIME - elapsed)
            if timer <= 0:
                reason = "Too slow! Time ran out."
                state = "gameover"

        if state == "start":
            draw_start_screen(screen, bg, font_title, font_sub)

        elif state == "gameover":
            draw_gameover_screen(screen, bg, font_title, font_sub, score, reason)

        elif state == "play":
            screen.blit(bg, (0, 0))
            customer.draw(screen)
            order.draw(screen, 75, 140)
            draw_panel(screen, pygame.Rect(0, SCREEN_H - 165, SCREEN_W, 165), (30, 10, 10), 200, 0)

            for btn in buttons:
                btn.check_hover(mouse_pos)
                btn.draw(screen)
                draw_text(screen, btn.item_name.capitalize(), font_ui, YELLOW,
                          btn.rect.centerx, SCREEN_H - 22, center=True)

            draw_panel(screen, pygame.Rect(10, 10, 150, 45), (20, 20, 20), 170)
            draw_text(screen, f"Score: {score}", font_ui, YELLOW, 20, 20)

            timer_color = (255, 80, 80) if timer < 2 else WHITE
            draw_panel(screen, pygame.Rect(SCREEN_W - 160, 10, 150, 45), (20, 20, 20), 170)
            draw_text(screen, f"⏱ {timer:.1f}s", font_ui, timer_color, SCREEN_W - 150, 20)
            draw_text(screen, "Order:", font_ui, YELLOW, 78, 118, center=True)

        pygame.display.flip()


if __name__ == "__main__":
    main()
