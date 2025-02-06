import pygame
import pygame_gui
import os

class Draw:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.panel_horizontal = pygame.image.load(os.path.join(src_loc,'../assets/images/panelHorizontal.png'))
        self.panel_vertical = pygame.image.load(os.path.join(src_loc,'../assets/images/panelVertical.png'))
        self.panel_length = self.panel_horizontal.get_width()
        self.panel_height = self.panel_horizontal.get_height()
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.button_scale = self.screen.get_width() * 0.2
        self.icon_scale = self.screen.get_height() * 0.05 
        self.center_space_x = self.screen.get_width() * 0.8
        self.string_length = self.screen_length // 16
        
        self.bg_top = pygame.image.load(os.path.join(src_loc,'../assets/images/bgtop.png'))
        self.bg_top = pygame.transform.scale(self.bg_top, (self.screen.get_width(), self.icon_scale + self.panel_height))
        self.bg_left = pygame.image.load(os.path.join(src_loc,'../assets/images/bgleft.jpg'))
        self.bg_left = pygame.transform.scale(self.bg_left, (self.button_scale, self.screen.get_height()))
        self.bg_right = pygame.image.load(os.path.join(src_loc,'../assets/images/bgright.jpg'))
        self.bg_right = pygame.transform.scale(self.bg_right, (self.button_scale, self.screen.get_height()))
        self.bg_workspaces = pygame.image.load(os.path.join(src_loc,'../assets/images/background2.jpg'))
        self.bg_workspaces = pygame.transform.scale(self.bg_workspaces, (1080*1.1,1364*1.1))
        self.funding = pygame.image.load(os.path.join(src_loc,'../assets/images/funding.png'))
        self.funding = pygame.transform.scale(self.funding, (self.icon_scale * 0.65, self.icon_scale * 0.65)) 
        self.reputation = pygame.image.load(os.path.join(src_loc,'../assets/images/reputation.png'))
        self.reputation = pygame.transform.scale(self.reputation, (self.icon_scale*0.65, self.icon_scale*0.65))
        self.observation = pygame.image.load(os.path.join(src_loc,'../assets/images/observation.png'))
        self.observation = pygame.transform.scale(self.observation, (self.icon_scale*0.65, self.icon_scale*0.65))
        self.telescope = pygame.image.load(os.path.join(src_loc,'../assets/images/telescope.png'))
        self.telescope = pygame.transform.scale(self.telescope, (self.icon_scale*0.65, self.icon_scale*0.65))
        self.achievement = pygame.image.load(os.path.join(src_loc,'../assets/images/achievement.png'))
        self.achievement = pygame.transform.scale(self.achievement, (self.icon_scale*0.65, self.icon_scale*0.65))
        self.score = pygame.image.load(os.path.join(src_loc,'../assets/images/score.png'))
        self.score = pygame.transform.scale(self.score, (self.icon_scale*0.65, self.icon_scale*0.65))
    
        
        
    def draw_background(self):
        self.screen.blit(self.bg_workspaces, (self.button_scale ,0))    
        
    def draw_frame(self):
        horizontal_number = self.screen_length // self.panel_length + 1
        vertical_number = self.screen_height // self.panel_length + 1
        for i in range(horizontal_number):
            self.screen.blit(self.panel_horizontal, (i*self.panel_length, 0))
            self.screen.blit(self.panel_horizontal, (i*self.panel_length, self.screen_height - self.panel_height))
        for i in range(vertical_number):
            self.screen.blit(self.panel_vertical, (0, i*self.panel_length))
            self.screen.blit(self.panel_vertical, (self.screen_length - self.panel_height, i*self.panel_length))    
        # -------------------------    
        
        for i in range(horizontal_number):
            self.screen.blit(self.panel_horizontal, (i*self.panel_length, self.icon_scale ))
        
        for i in range(vertical_number):
            self.screen.blit(self.panel_vertical, (self.button_scale, i*self.panel_length))    
            
        for i in range(vertical_number):
            self.screen.blit(self.panel_vertical, (self.center_space_x, i*self.panel_length))   
            
    def draw_bg(self):  
        self.screen.blit(self.bg_left, (0, 0))
        self.screen.blit(self.bg_right, (self.center_space_x, 0))  
        self.screen.blit(self.bg_top, (0, 0))   
            
     
    def draw_text(self, text, x, y, color=None, size=36):
        font = pygame.font.Font(None, size)
        if color==None:
            text = font.render(str(text), True, (255, 255, 255))
        else:
            text = font.render(str(text), True, color=color)
        self.screen.blit(text, (x, y))    
            
    def draw_status(self,player):
        x_init = self.button_scale + self.panel_height 
        x_space = self.icon_scale + self.string_length
        self.screen.blit(self.funding, (x_init, self.panel_height*1.15)) 
        self.screen.blit(self.observation, (x_init+x_space, self.panel_height*1.15))     
        self.screen.blit(self.telescope, (x_init+x_space*2, self.panel_height*1.15)) 
        self.screen.blit(self.reputation, (x_init+x_space*3, self.panel_height*1.15))        
        self.screen.blit(self.achievement, (x_init+x_space*4, self.panel_height*1.15))
        self.screen.blit(self.score, (x_init+x_space*5, self.panel_height*1.15))
        
        player_status = player.get_status()
        self.draw_text(player_status[2], x_init + self.icon_scale*0.8, self.panel_height*1.7)
        self.draw_text(player_status[1], x_init + x_space + self.icon_scale*0.8, self.panel_height*1.7)
        self.draw_text(player_status[4], x_init + x_space*2 + self.icon_scale*0.8, self.panel_height*1.7)
        self.draw_text(player_status[3], x_init + x_space*3 + self.icon_scale*0.8, self.panel_height*1.7)
        self.draw_text(player_status[5], x_init + x_space*4 + self.icon_scale*0.8, self.panel_height*1.7)
        self.draw_text(player_status[6], x_init + x_space*5 + self.icon_scale*0.8, self.panel_height*1.7)
        
    def draw_title(self, player):
        if player.score < 50:
            self.draw_text(f'BSc. {player.name}', self.icon_scale*0.5, self.panel_height*1.7)
        elif player.score < 100:
            self.draw_text(f'MSc. {player.name}', self.icon_scale*0.5, self.panel_height*1.7)
        elif player.score < 200:
            self.draw_text(f'PhD. {player.name}', self.icon_scale*0.5, self.panel_height*1.7)
        else:
            self.draw_text(f'Prof. {player.name}', self.icon_scale*0.5, self.panel_height*1.7)

             
        