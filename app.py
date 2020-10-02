import pygame
from pygame import display, event
import random 
from time import sleep
import numbers_class as num
from numbers_class import Numbers
import logic

pygame.init()

display.set_caption('Simple 2408')

screen = display.set_mode((512, 512))
screen.fill((255,255,255))
screen.blit(screen, (0,0))
display.flip()

board = logic.start_game()
def tiles_change(board):
    tiles = []
    for i in range(4):
        for j in range(4):
            tiles.append(Numbers(board,i,j))
    return tiles
tiles = tiles_change(board)


running = True
while running:
    current_events = event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
    changed = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        board, changed = logic.move_left(board)
    elif keys[pygame.K_RIGHT]:
        board, changed = logic.move_right(board)
    elif keys[pygame.K_UP]:
        board, changed = logic.move_up(board)
    elif keys[pygame.K_DOWN]:
        board, changed = logic.move_down(board)

    tiles = tiles_change(board)

    status = logic.current_state(board)
    print(status)
    if status == 'Continue':
        if changed:
            board = logic.add_new_number(board)
            tiles = tiles_change(board)
        else:
            pass
    else:
        sleep(2)
        if status == 'Game over':
            screen.blit(num.lose, (0,0))
        else:
            logic.current_state(board)
            screen.blit(num.win, (0,0))
        display.flip()
        sleep(2)
        running = False

    screen.fill((225,225,225))
    
    for tile in tiles:  
        rect = pygame.draw.rect(
            screen, tile.rgb, 
            (tile.col*num.image_size + num.margin, 
             tile.row*num.image_size + num.margin, 
             num.image_size - 2*num.margin, 
             num.image_size - 2*num.margin), 
             4)
        if tile.name == 0:
            screen.blit(
                tile.box, 
                (tile.col*num.image_size + num.margin,
                tile.row*num.image_size + num.margin))
        else:
            screen.blit(
                tile.text, 
                (tile.text_x,
                tile.text_y))
        
    display.flip()
   
print('Goodbye!')
