import pygame
import matplotlib.pyplot as plt
import numpy as np
import pygame_gui
import random
import os

class ManageObservations:
    def __init__(self, screen, manager, message):
        self.screen = screen
        self.manager = manager
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.icon_scale = self.screen.get_height() * 0.05
        self.calender_frame = pygame.image.load(os.path.join(src_loc,os.path.join(src_loc,'../assets/images/frame1.png')))
        self.pin = pygame.image.load(os.path.join(src_loc,os.path.join(src_loc,'../assets/images/pushpin.png')))
        self.pin = pygame.transform.scale(self.pin, (32,32))
        self.days = 0
        self.message = message
        
        
        

    def create_calender(self,week,only_calender=False):
        src_loc = os.path.dirname(os.path.abspath(__file__))
        weeks = [f'Week '+str(week), f'Week '+str(int(week+1)), f'Week '+str(int(week+2)), f'Week '+str(int(week+3)),f'Week '+str(int(week+4))]
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        tabel_color = '#FFFFE0'
        fig, ax = plt.subplots(figsize=(10, 6),facecolor=tabel_color)
        table = ax.table(cellText=np.full((5, 7), ''), 
                     rowLabels=weeks, 
                     colLabels=days, 
                     loc='center', 
                     cellLoc='center', 
                     colWidths=[0.11] * 7,
                     rowColours=[tabel_color]*5,
                     colColours=[tabel_color]*7,
                     cellColours=[[tabel_color]*7]*5)

        table.auto_set_font_size(False)
        table.set_fontsize(12)
        for key, cell in table.get_celld().items():
            cell.set_edgecolor('black')
            cell.set_linewidth(1)
        table.scale(1, 3)
        ax.axis('off')
        plt.title('Manage Observations in the Coming 5 Weeks', fontsize=16, fontweight='bold', pad=0, y=0.9)
        plt.savefig(os.path.join(src_loc,'../tmp/images/calender.png'))
        plt.close()
        self.calender = pygame.image.load(os.path.join(src_loc,'../tmp/images/calender.png'))
        self.calender_width = self.calender.get_width()
        self.calender_height = self.calender.get_height()
        self.x_calender = self.screen_length/2 - self.calender_width/2
        self.y_calender = self.screen_height/3
        
        self.buttons = []
        for i in range(5):
            for j in range(7):
                x = self.screen_length/2 - 255 + j*85
                y = self.screen_height/3 + 215 + i*50
                self.button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((x, y), (30, 30)),
                    text=' ',
                    manager=self.manager,
                    object_id='#button_calender'
                )
                self.buttons.append(self.button)
        self.buttons = np.array(self.buttons).reshape(5, 7)    
        self.selected_days = np.zeros_like(self.buttons)
        
        if not only_calender:
            self.days_number_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((self.x_calender + 180, self.y_calender + self.calender_height - 155), (90, 90)),
                text=f'x {self.days}',
                manager=self.manager,
                object_id='#label_black'
            )
        
        # draw back button
            self.back_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((self.x_calender + self.calender_width - 240, self.y_calender + self.calender_height - 130), (90, 45)),
                text='Back',
                manager=self.manager,
                object_id='#button_black'
            )
    
        
    def draw_calender(self):
        self.screen.blit(self.calender, (self.x_calender, self.y_calender))
        
        # draw frame
        self.calender_frame = pygame.transform.scale(self.calender_frame, (self.calender_width, self.calender_height))
        self.screen.blit(self.calender_frame, (self.x_calender, self.y_calender))
        # draw pin
        self.screen.blit(self.pin, (self.x_calender + 160, self.y_calender + self.calender_height - 120)) 
        
        
        
    def show_all(self):
        for i in range(5):
            for j in range(7):
                self.buttons[i, j].show()
        self.days_number_label.show()
        self.back_button.show()        

    
    def draw(self):
        self.manager.draw_ui(self.screen)    
                
                
    def hide_all(self):
        for i in range(5):
            for j in range(7):
                self.buttons[i, j].hide()
        self.days_number_label.hide()
        self.back_button.hide()        
             
    def hide_all_calender_buttons(self):
        for i in range(5):
            for j in range(7):
                self.buttons[i, j].hide()
                 
                
    def update(self, time_delta, date, player):
        self.manager.update(time_delta)    
        self.days_number_label.set_text(f'x {self.days}')
        for i in range(5):
            for j in range(7):                    
                if (i < ((date[0]-1)%5+1) and j < ((date[1]-1)%7+1)) or i < ((date[0]-1)%5):
                    if self.buttons[i, j].is_selected:
                        player.observations += random.random() * player.telescope 
                        self.message.update(time_delta, date, f'You observed tonight.')
                    self.buttons[i, j].disable()   
        
             
           
    def manage(self, event, player):
        event_name = event.ui_element
        show_manage_observations = True
        if player.observation_time > 0:
            for i in range(5):
                for j in range(7):
                    if event_name == self.buttons[i, j]:
                        if self.selected_days[i, j] == 0:
                            self.selected_days[i, j] = 1
                            player.observation_time -= 1
                            self.buttons[i, j].select()
                        elif self.selected_days[i, j] == 1:
                            self.selected_days[i, j] = 0
                            player.observation_time += 1
                            self.buttons[i, j].unselect()
        elif player.observation_time == 0:
            for i in range(5):
                for j in range(7):
                    if event_name == self.buttons[i, j]:
                        if self.selected_days[i, j] == 1:
                            self.selected_days[i, j] = 0
                            player.observation_time += 1
                            self.buttons[i, j].unselect()
                            
        if event_name == self.back_button:
            self.hide_all()
            show_manage_observations = False
            
        return show_manage_observations        
                            
"""    def disable_observation(self, player, date, time_delta):

        for i in range(5):
            for j in range(7):                    
                if i < ((date[0]-1)%5+1) and j < ((date[1]-1)%7+1):
                    if self.buttons[i, j].is_selected:
                        player.observations += random.random() * player.telescope 
                        self.message.update(time_delta, date, f'You observed tonight.')
                    self.buttons[i, j].disable()   """
          
                            