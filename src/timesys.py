import pygame
import pygame_gui
import time
from draw import Draw
import numpy as np

class Time:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager
        h_button = 60
        self.button_scale = self.screen.get_width() * 0.2
        self.icon_scale = self.screen.get_height() * 0.05
        self.center_space_x = self.screen.get_width() * 0.8
        self.Draw = Draw(self.screen, self.manager)
        self.panel_height = self.Draw.panel_height
        self.button_scale_new = self.button_scale - self.panel_height - self.screen.get_width() * 0.02
        self.pause = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.center_space_x * 1.15, 17), (self.button_scale_new*0.4, h_button*0.7)),
            text='Pause',
            manager=self.manager,
            object_id='#button_calender'
        )
        self.time_0 = time.time()
        self.paused = False
        self.deltat = 0
        self.week_0 = 0
        
    def get_date(self):
        self.time_1 = time.time()
        if not self.paused:
            self.deltat += self.time_1 - self.time_0
        else:
            self.deltat = self.deltat
        self.time_0 =  time.time()    
        date = self.deltat // 2
        return date
    
    
    def Pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause.set_text('Resume')
        else:
            self.pause.set_text('Pause')
            
            
    def update(self, time_delta):
        self.manager.update(time_delta)
        
    def draw(self):
        self.manager.draw_ui(self.screen)

    def hide_all(self):
        self.pause.hide()
        
        
    def show_all(self):
        self.pause.show()        
        
    def draw_date(self):
        date = self.get_date()
        week = int(date // 7 + 1)
        day = int(date % 7 + 1)
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        date = f'Week {week} - {days[day-1]}'
        self.Draw.draw_text(date, self.center_space_x + self.panel_height*2, self.panel_height*1.7) 
        
    def get_day(self):
        date = self.get_date()
        week = int(date // 7 + 1)
        day = int(date % 7 + 1)
        return np.array([week,day])
    
    def update_calender(self):
        self.week_1 = self.get_day()[0] - 1
        if self.week_1 % 5 == 0 and self.week_1 > self.week_0:
            new_calender = True
        else:
            new_calender = False
        self.week_0 = self.get_day()[0] - 1    
        return new_calender
                    
    
        
        