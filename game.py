import pygame 
import random 
import json
import os

pygame.init()

WIDTH, HEIGHT = 800, 400
FPS = 60

score = 0
high_score = 0
show_new_high_score = False
show_new_high_score_time = 0
SCORE_RATE = 5

GREEN = (34, 177, 76)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
RED = (255, 0, 0)          
GRAY = (120, 120, 120)     
BLUE = (0, 100, 255)      
BLACK = (0, 0, 0)

GROUND_HEIGHT = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
INIT_SPEED = 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background_img = pygame.image.load("StartBG.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

background1_img = pygame.image.load("Background.png").convert()
background1_img = pygame.transform.scale(background1_img, (WIDTH, HEIGHT))

player_image = pygame.image.load("Player2.png").convert()
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))

ground_img = pygame.image.load("Ground.png").convert_alpha()
groung_img = pygame.transform.scale(ground_img, (WIDTH, GROUND_HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey Run")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,60)
small_font = pygame.font.SysFont(None, 32)

login_button = pygame.Rect(WIDTH - 100, 10, 80, 30)
ground_scroll_x = 0

class Player:
    def __init__(self):
        self.image = pygame.image.load("Player2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = HEIGHT - GROUND_HEIGHT - self.rect.height + 10 
        self.vel_y = 0
        self.jump_count = 0 
        self.on_island = False 

def update(self):
    self.vel_y +=1
    self.rect.y += self.v_y
    
    if self.rect.bottom >= HEIGHT - GROUND_HEIGHT:
        self.rect.bottom = HEIGHT - GROUND_HEIGHT
        self.vel_y = 0
        self.jump_count = 0
        self. on_island = False
        
def jump(self):
    if self.jump_count < 2:
        if self.jump_count == 0:
            self.vel_y = -15
    elif self.jump_count == 1:
        self.vel_y = -20
    self.jump_count += 1 
    self.on_island = False 
    
def draw(self, surface):
    surface.blit(self.image, self.rect)
    
class Obstacle: 
    def __init__(self, type_):
        self.type = type_
        if type == 'rock':
            self.width = PLAYER_WIDTH + 50
            self.height = PLAYER_HEIGHT - 20
            self.image = pygame.image.load("snake.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.rect = self.image.get_rect()
            self.rect.x = WIDTH
            self.rect.y = HEIGHT - GROUND_HEIGHT - self.height + 10
        
        elif type_ == 'floating':
            self.width = PLAYER_WIDTH + 60 
            self.height = PLAYER_HEIGHT + 10
            self.image = pygame.image.load("float.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.rect = pygame.Rect(WIDTH, HEIGHT - GROUND_HEIGHT - self.height -140, self.width, self.height)
        
        elif type_ == 'lake':
            self.width = 100
            self.height = GROUND_HEIGHT + 30
            self.image = pygame.image.load("lake.png").convert_alpha()
            self.image = pygame.transform.sclae(self.image, (self.width, self.height))
            self.rect = pygame.Rect(WIDTH, HEIGHT - GROUND_HEIGHT - self.height, self.width, self.height)
    
    
    def move(self, speed):  
        if self.type == 'floating':
            self.rect.x -= speed * 1.5
        elif self.type == 'rock':
            self.rect.x -+ speed * 1.75
        else:
            self.rect.x -= speed
            
    def draw(self, surface): 
        if hasattr(self, 'image'):
            surface.blit(self.image, self.rect)
        else:pygame.draw.rect(surface, (255, 0, 0), self.rect)
        
    
                