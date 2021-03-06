import pygame
from pygame.sprite import Sprite

class bullet(Sprite):
	def __init__(self,screen, the_player, direction):
		super(bullet, self).__init__()
		self.screen = screen

		self.rect = pygame.Rect(0,0,2,8)
		self.color = (0,0,0)
		self.rect.centerx = the_player.x
		self.rect.top = the_player.y
		self.speed = 15
		self.direction = direction
		self.x = self.rect.x
		self.y = self.rect.y




	def update(self):
		if self.direction == 1: #up
			self.y -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		elif self.direction == 2: #right
			self.x += self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position
		elif self.direction == 3: #down
			self.y += self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		else:
			self.x -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect) #draw the bullet!}
