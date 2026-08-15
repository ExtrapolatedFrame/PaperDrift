# import code
import sys
import pygame
import random
import math

# import player.py
from player import Player
print("Imported Player module!")

# initalise
pygame.init()
pygame.display.set_caption("Nova Drift - Temu edition")

# config
targetfps = 120
fullscreen = False
debugMode = True

# variables
gameTickSpeed = 60
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
player = Player(0,0, 0, 10, 10)
print("Player created!")

# functions
def changeWindowSize(x,y,z):
    if z:
        return pygame.display.set_mode((x,y), pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((x,y))

window = changeWindowSize(640,360,False)

run = True

print("Game loop started!")
while run:
    # variabless
    mouseX, mouseY = pygame.mouse.get_pos()

    #single input  press:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # fullscreen toggle
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            fullscreen = not fullscreen
            if fullscreen:
                changeWindowSize(0,0,True)
            else:
                changeWindowSize(640,360,False)   

    # rainbow window.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    window.fill((0,0,0))

    clock.tick(targetfps)
    fps = clock.get_fps()
    if fps > 0:
        deltaTime = gameTickSpeed / fps    

    # render debug text    
    if debugMode:
        if fps > 0:  
            deltaTimeCounter = font.render(f"DeltaTime: {deltaTime:.2f}", True, (255,255,255))
            window.blit(deltaTimeCounter, (110,0))

        fpsCounter = font.render(f"FPS: {fps:.0f}", True, (255,255,255))
        window.blit(fpsCounter, (0,0))

        playerCoords = font.render(f"X: {player.x:.0f} Y: {player.y:.0f}", True, (255,255,255))
        window.blit(playerCoords, (0,25))

        playerVel = font.render(f"Xvel: {player.Xvel:.2f} Yvel: {player.Yvel:.2f}", True, (255,255,255))
        window.blit(playerVel, (0,50))

    playerTemp = font.render(f"{player.dir:.0f}", True, (255, 255, 255))
    window.blit(playerTemp, (player.x,player.y))  

    if fps > 0:
        player.Xvel = player.Xvel * 0.94 ** (deltaTime * targetfps)
        player.Yvel = player.Yvel * 0.94 ** (deltaTime * targetfps)

        player.x += player.Xvel * deltaTime
        player.y += player.Yvel * deltaTime


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]: player.move(2)

    player.turn(mouseX, mouseY)

    # check where player is
    if player.x >= 1280: player.x = 1
    if player.x <= 0:    player.x = 1279
    if player.y >= 720:  player.y = 1
    if player.y <= 0:    player.y = 719
        

    # print to window
    pygame.display.flip()

pygame.quit()
sys.exit()