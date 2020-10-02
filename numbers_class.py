import os
import random
import pygame
from pygame import image, transform

image_size = 128
margin = 8

won = image.load('images/win.jpg')
win = won.copy()
win = transform.scale(won, (512,512))

lost = image.load('images/lose.png')
lose = lost.copy()
lose = transform.scale(lose, (512,512))

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
      if self.name < 10:
        self.text_x = self.col*image_size + image_size/2 - margin
      elif self.name > 10 and self.name < 100:
        self.text_x = self.col*image_size + image_size/2 - margin*2
      elif self.name > 100 < 1000:
        self.text_x = self.col*image_size + image_size/2 - margin*4
      else:
        self.text_x = self.col*image_size + image_size/2 - margin*8
      self.text_y = self.row*image_size + image_size/2 - 45/2
      self.image = image.load('images/matched.png')
      self.image = transform.scale(self.image, (image_size - 2*margin, image_size - 2*margin))
      self.box = self.image.copy()
      self.box.fill((150,150,150))