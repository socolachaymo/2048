import os
import random
import pygame
from pygame import image, transform

image_size = 128
screen_size = 512
num_tiles_side = 4
num_tiles_total = 16
margin = 8

numbers = [2,4,8,16,32,64,128,256,512,1024,2048]

won = image.load('images/win.jpg')
win = won.copy()
win = transform.scale(won, (512,512))

lost = image.load('images/lose.png')
lose = lost.copy()
lose = transform.scale(won, (512,512))

class Numbers:
  def __init__(self, board, r, c):
      self.index = r*4 + c
      self.row = r
      self.col = c
      self.name = board[r][c]
      self.rgb = (195,0,0)

      pygame.font.init()
      self.font = pygame.font.SysFont('arial', 45)
      self.text = self.font.render(str(self.name), True, (255,255,255),(0,255,0))
      self.textRect = self.text.get_rect() 
      self.textRect.center = (0, 0)
      self.image = image.load('images/matched.png')
      self.image = transform.scale(self.image, (image_size - 2*margin, image_size - 2*margin))
      self.box = self.image.copy()
      self.box.fill((150,150,150))
      self.skip = False

