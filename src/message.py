import pygame
import pygame_gui
import time
from draw import Draw
import numpy as np
from music import Music
class Message:
    def __init__(self, screen, manager, silence=True):
        self.screen = screen
        self.manager = manager
        h_button = 60
        self.music = Music(self.screen, self.manager)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.button_scale = self.screen.get_width() * 0.2
        self.icon_scale = self.screen.get_height() * 0.05
        self.center_space_x = self.screen.get_width() * 0.8
        self.Draw = Draw(self.screen, self.manager)
        self.panel_height = self.Draw.panel_height
        self.button_scale_new = self.button_scale - self.panel_height - self.screen.get_width() * 0.02
        self.message_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((self.center_space_x + self.panel_height*2, self.panel_height*1.7+60), (self.screen_width/6, self.screen_height-110)),
            html_text='<p>Message Box</p>',
            manager=self.manager,
            object_id='#message'
        )
        self.message_box.append_html_text('<p>'+'-'*40+'</p>')

            
    def update(self, time_delta, day, message=None):
        self.manager.update(time_delta)
        week = day[0]
        day = day[1]
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        date = f'Week {week} - {days[day-1]}'
        if not message == None:
            self.music.play_bell()
            message = '<p>'+ date + ' ---- ' + message + '</p>'
            self.message_box.append_html_text(message)
            self.message_box.append_html_text('<p>'+'-'*40+'</p>')
        
    def draw(self):
        self.manager.draw_ui(self.screen)

    def hide_all(self):
        self.message_box.hide()
        pass
        
        
    def show_all(self):    
        self.message_box.show()
        pass
        
    
        
        