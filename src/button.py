import pygame
import pygame_gui
from draw import Draw

class Button:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager
        h_button = 60
        self.Draw = Draw(self.screen, self.manager)
        self.button_scale = self.screen.get_width() * 0.2
        self.icon_scale = self.screen.get_height() * 0.05
        self.panel_height = self.Draw.panel_height
        self.panel_length = self.Draw.panel_length
        self.center_space_x = self.screen.get_width() * 0.8
        
        init_x = self.panel_height + self.screen.get_width() * 0.01
        init_y = self.icon_scale + self.panel_height + self.screen.get_height() * 0.01
        self.button_scale_new = self.button_scale - self.panel_height - self.screen.get_width() * 0.02
        self.shop = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((init_x, init_y), (self.button_scale_new, h_button)),
            text='Shop',
            manager=self.manager
        )
        
        self.manage_observations = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((init_x, init_y + h_button), (self.button_scale_new, h_button)),
            text='Manage Observations',
            manager=self.manager
        )
        
        self.research = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((init_x, init_y + h_button*2), (self.button_scale_new, h_button)),
            text='Research',
            manager=self.manager
        )
        
        self.learn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((init_x, init_y + h_button*3), (self.button_scale_new, h_button)),
            text='Learn',
            manager=self.manager
        )
        
        self.conference = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((init_x, init_y + h_button*4), (self.button_scale_new, h_button)),
            text='Conference',
            manager=self.manager
        )   
        
        self.apply_funding = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((init_x, init_y + h_button*5), (self.button_scale_new, h_button)),
            text='Apply for Funding',
            manager=self.manager
        )
        
        self.classification = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((init_x, init_y + h_button*6), (self.button_scale_new, h_button)),
            text='Classification (bonus)',
            manager=self.manager
        )
        
        self.save_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((init_x, init_y + h_button*7), (self.button_scale_new, h_button)),
            text='Save',
            manager=self.manager
        )
        
        self.exit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((init_x, init_y + h_button*8), (self.button_scale_new, h_button)),
            text='Exit',
            manager=self.manager
        )
        
        
        
    def update(self, time_delta):
        self.manager.update(time_delta)
        
    def draw(self):
        self.manager.draw_ui(self.screen)

    def hide_all(self):
        self.manage_observations.hide()
        self.shop.hide()
        self.learn.hide()
        self.research.hide()
        self.conference.hide()
        self.classification.hide()
        self.apply_funding.hide()
        self.exit_button.hide()
        self.save_button.hide()
        
    def show_all(self):
        self.manage_observations.show()
        self.shop.show()
        self.learn.show()
        self.research.show()
        self.conference.show()
        self.classification.show()
        self.apply_funding.show()
        self.exit_button.show()
        self.save_button.show()
        

        
