import pygame
import random
import Player
import Satelite

pygame.init()

pygame.display.set_caption("GPS Simulator")

WIDTH = 1000 
HEIGHT = 1000

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

player = Player.Player(400, 300, 5)

satelite1 = Satelite.Satelite(random.randint(0, WIDTH), random.randint(0, HEIGHT))
satelite2 = Satelite.Satelite(random.randint(0, WIDTH), random.randint(0, HEIGHT))
satelite3 = Satelite.Satelite(random.randint(0, WIDTH), random.randint(0, HEIGHT))

# Initializing the font
font = pygame.font.SysFont("Arial", 20)
img1 = font.render("Space to stop the satelites", True, (255, 255, 255))
img2 = font.render("Z to increase speed", True, (255, 255, 255))
img3 = font.render("X to decrease speed", True, (255, 255, 255))
img4 = font.render("ESC to quit", True, (255, 255, 255))

is_running = True
satelites_moving = True

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                satelites_moving = not satelites_moving

            if event.key == pygame.K_z:
                satelite1.change_speed(1)
                satelite2.change_speed(1)
                satelite3.change_speed(1)
            
            if event.key == pygame.K_x:
                satelite1.change_speed(-1)
                satelite2.change_speed(-1)
                satelite3.change_speed(-1)
            
            if event.key == pygame.K_ESCAPE:
                is_running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move("D")
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move("A")
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        player.move("W")
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move("S")

    if satelites_moving:
        satelite1.move(WIDTH, HEIGHT)
        satelite2.move(WIDTH, HEIGHT)
        satelite3.move(WIDTH, HEIGHT)


    window_surface.fill((0, 0, 0))

    img5 = font.render(f"Speed: {round(satelite1.speed*10)}", True, (255, 255, 255))

    window_surface.blit(img1, (10, 0))
    window_surface.blit(img2, (10, 20))
    window_surface.blit(img3, (10, 40))
    window_surface.blit(img4, (10, 60))
    window_surface.blit(img5, (10, HEIGHT-25))

    # Drawing the player
    pygame.draw.circle(window_surface, pygame.Color("red"), (player.x, player.y), 5)


    # Drawing the satelites
    pygame.draw.circle(window_surface, pygame.Color(satelite1.r, satelite1.g, satelite1.b), (satelite1.x, satelite1.y), 5)
    pygame.draw.circle(window_surface, pygame.Color(satelite2.r, satelite2.g, satelite2.b), (satelite2.x, satelite2.y), 5)
    pygame.draw.circle(window_surface, pygame.Color(satelite3.r, satelite3.g, satelite3.b), (satelite3.x, satelite3.y), 5)

    # Drawing the circumferences of the satelites
    pygame.draw.circle(window_surface, pygame.Color(satelite1.r, satelite1.g, satelite1.b), (satelite1.x, satelite1.y), satelite1.distance(player), 1)
    pygame.draw.circle(window_surface, pygame.Color(satelite2.r, satelite2.g, satelite2.b), (satelite2.x, satelite2.y), satelite2.distance(player), 1)
    pygame.draw.circle(window_surface, pygame.Color(satelite3.r, satelite3.g, satelite3.b), (satelite3.x, satelite3.y), satelite3.distance(player), 1)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()