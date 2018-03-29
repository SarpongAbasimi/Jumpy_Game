import pygame
from settings import*
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image =pygame.Surface((30,40))
        self.image.fill(yellow)
        self.rect =self.image.get_rect()
        self.pos = vec(width/2 ,height/2)
        self.vel = vec(0,0)
        self.acc =(0,0)
    def jump(self):
        #jump only when standing on platform
        self.rect.x +=1
        hits =pygame.sprite.spritecollide(self,self.game.platform,False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -15
        

    def update(self):
        self.acc = vec(0,player_gravity)
        keys =pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -player_acc
        if keys[pygame.K_RIGHT]:
            self.acc.x = player_acc

        self.acc.x += self.vel.x*player_friction
        self.vel += self.acc
        self.pos += self.vel+0.5*self.acc
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x =width
             
        #new posiiton
        self.rect.midbottom =self.pos

class platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(green)
        self.rect =self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        
        
        
        
