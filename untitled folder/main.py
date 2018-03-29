import pygame
import random
from settings import*
from sprites import*
  
class Game:
    def __init__(self):
        #initialize game window
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Jumpy")
        self.clock = pygame.time.Clock()
        self.running =True
        self.font_name = pygame.font.match_font(font_name)
    def new(self):
        self.score=0
        self.all_sprites = pygame.sprite.Group()
        self.platform =pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in platform_list:#explode the list
            p =platform(*plat)
            self.all_sprites.add(p)
            self.platform.add(p)
        
        #p1 = platform(0,height-40,width,40) 
        #self.all_sprites.add(p1)
        #self.platform.add(p1)
        #p2 = platform(width/2 -50, height* 3/4,100,20)
        #self.all_sprites.add(p2)
        #self.platform.add(p2)
        
        self.run()

    def run(self):
        self.clock.tick(fps)
        self.playing =True  
        while self.playing: 
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()
    def update(self):
            self.all_sprites.update()
            if self.player.vel.y > 0:            
                hits = pygame.sprite.spritecollide(self.player,self.platform,False)
                if hits:
                    self.player.pos.y = hits[0].rect.top+1
                    self.player.vel.y = 0
            if self.player.rect.top <= height/4:
                self.player.pos.y += abs(self.player.vel.y)
                for plat in self.platform:
                    plat.rect.y += abs(self.player.vel.y)
                    if plat.rect.top >= height:
                        plat.kill()
                        self.score += 10

            if self.player.rect.bottom > height:
                for sprite in self.all_sprites:
                    sprite.rect.y -= max(self.player.vel.y,10)
                    if sprite.rect.bottom < 0:
                        sprite.kill()
            if len(self.platform) == 0:
                self.playing = False
                

            #spawn new platform to keep the same average of platforms.
            while len(self.platform) <6:
                wi =random.randrange(50,100)
                hi = random.randrange(10,15)
                p = platform(random.randrange(0,width -wi),
                             random.randrange(-75,-30),wi,hi)
                self.platform.add(p)
                self.all_sprites.add(p)
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing =False
                self.running =False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                
    def draw(self):
        self.screen.fill(bgcolor)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score),22,white,width/2,15)
        pygame.display.flip()
        
    def show_start_screen(self):
        self.screen.fill(bgcolor)
        self.draw_text("Jumpy",48,white,width/2,height/4)
        self.draw_text("Arrows to move,space to jump",22,white,width/2,height/2)
        self.draw_text("press a key to play", 22,white,width/2,height*3/4)
        pygame.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        pass
    
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
        
        pass
    def draw_text(self,text,size,color,x,y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
    
