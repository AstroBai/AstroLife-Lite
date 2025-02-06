import pygame
import matplotlib.pyplot as plt
import numpy as np
import pygame_gui
from draw import Draw
import random
import os
import glob
import json

class Classification:
    def __init__(self, screen, manager, message, player):
        self.screen = screen
        self.manager = manager
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.Draw = Draw(self.screen,self.manager)
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.classification_index = player.classification_index
        self.message = message
        self.get_pic_names()
        self.galaxy_class = ['Elliptical', 'Lenticular', 'Spiral', 'Bared Spiral', 'Irregular', 'Merger']
        
        self.elliptical = pygame.image.load(os.path.join(src_loc,'../assets/images/elliptical.png'))
        self.lenticular = pygame.image.load(os.path.join(src_loc,'../assets/images/lenticular.png'))
        self.spiral = pygame.image.load(os.path.join(src_loc,'../assets/images/spiral.png'))
        self.bared_spiral = pygame.image.load(os.path.join(src_loc,'../assets/images/baredspiral.png'))
        self.irregular = pygame.image.load(os.path.join(src_loc,'../assets/images/irregular.png'))
        self.merger = pygame.image.load(os.path.join(src_loc,'../assets/images/merger.png'))
        
        self.selected_image = self.elliptical
        
        save_name = player.name + '_classification.json'
        self.classification_save_file = os.path.join(src_loc, '../saves', save_name)
        
        self.load_classification_data(player)
        
        
        
        
        
        
    def get_pic_names(self):
        src_loc = os.path.dirname(os.path.abspath(__file__))
        data_loc = os.path.join(src_loc, '../galaxy_data/gz2/images')
        for dirpath, dirnames, filenames in os.walk(data_loc):
            self.image_files = glob.glob(os.path.join(dirpath, '*.jpg'))
            self.image_files.sort()                
            
        
        
    def create_classification(self, only_classification=False):
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.classification = pygame.image.load(os.path.join(src_loc,'../assets/images/bgclassification.png'))
        
        self.classification_width = self.classification.get_width() *3.5
        self.classification_height = self.classification.get_height() *3.5
        self.classification = pygame.transform.scale(self.classification, (self.classification_width, self.classification_height))
        self.x_classification = self.screen_length/2 - self.classification_width/2
        self.y_classification = self.screen_height/3 - 250
    
        
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_classification + self.classification_width - 220, self.y_classification + self.classification_height - 100), (90, 45)),
            text='Back',
            manager=self.manager,
            object_id='#button_white'
        )
        
        self.select = pygame_gui.elements.UIDropDownMenu(
            options_list=self.galaxy_class,
            starting_option='Elliptical',
            relative_rect=pygame.Rect((self.screen_length/2-100, self.screen_height/2 + 75), (200, 40)),
            manager=self.manager
        )

        self.next_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.screen_length/2 + 100, self.screen_height/2 + 75), (90, 40)),
            text='Next',
            manager=self.manager,
            object_id='#button_white'
        )
        
        self.previous_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.screen_length/2 -190, self.screen_height/2 + 75), (90, 40)),
            text='Last',
            manager=self.manager,
            object_id='#button_white'
        )
        
        self.submit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.screen_length/2 - 90, self.screen_height/2 + 370), (180, 45)),
            text='Submit',
            manager=self.manager,
            object_id='#button_white'
        )
        
    def draw_classification(self):
        self.galaxy_picture = pygame.image.load(self.image_files[self.classification_index])
        self.galaxy_picture = pygame.transform.scale(self.galaxy_picture, (self.galaxy_picture.width*1.5 , self.galaxy_picture.height*1.5))
        
        
        self.x_picture = self.screen_length/2 - self.galaxy_picture.get_width()/2
        self.y_picture = self.screen_height/3 - 250
        
        
        self.screen.blit(self.galaxy_picture, (self.x_picture, self.y_picture))
        
        self.screen.blit(self.classification, (self.x_classification, self.y_classification))
        
        self.selected_image = pygame.transform.scale(self.selected_image, (self.selected_image.width * 160/self.selected_image.height,160))
        self.x_image = self.screen_length/2 - self.selected_image.get_width()/2
        self.y_image = self.screen_height/3 + 400
        self.screen.blit(self.selected_image, (self.x_image, self.y_image ))
        
        
        
        
        
          
        
    def show_all(self):
        self.back_button.show()     
        self.select.show()
        self.next_button.show()
        self.previous_button.show()    
        self.submit_button.show()    

    
    def draw(self):
        self.manager.draw_ui(self.screen)    
                
                
    def hide_all(self):
        self.back_button.hide()     
        self.select.hide()
        self.next_button.hide()    
        self.previous_button.hide()    
        self.submit_button.hide() 

                
    def update(self, time_delta, player):
        self.classification_index = player.classification_index
        self.image_name = self.image_files[self.classification_index]    
        self.manager.update(time_delta)    
        self.selected = self.select.selected_option[1]
        self.submit_button.enable()
        self.submit_button.set_text('Submit')
        if not self.classification_data[self.image_name[-22:-4]] == 'None':
            self.submit_button.disable()
            self.submit_button.set_text('Submitted')
        
        if self.selected == 'Elliptical':
            self.selected_image = self.elliptical
            self.bonus = 5
        elif self.selected == 'Lenticular':
            self.selected_image = self.lenticular
            self.bonus = 8
        elif self.selected == 'Spiral':
            self.selected_image = self.spiral
            self.bonus = 10
        elif self.selected == 'Bared Spiral':
            self.selected_image = self.bared_spiral
            self.bonus = 10
        elif self.selected == 'Irregular':
            self.selected_image = self.irregular
            self.bonus = 8
        elif self.selected == 'Merger':
            self.selected_image = self.merger
            self.bonus = 15
        
        
             
           
    def manage(self, event, player, time_delta, day):
        event_name = event.ui_element
        classifying = True
        if event_name == self.back_button:
            self.hide_all()
            classifying = False
            self.save_classification_data()
            
        
        if event_name == self.next_button:
            player.classification_index += 1
            
        if event_name == self.previous_button:
            player.classification_index -= 1
        
        if player.classification_index >= len(self.image_files):
            player.classification_index = 0
        if player.classification_index < 0:
            player.classification_index = len(self.image_files) - 1
                     
        if event_name == self.submit_button:
            self.classification_data[self.image_name[-22:-4]] = self.selected
            player.funding += self.bonus
            self.message.update(time_delta, day, f'Funding increased by ${self.bonus} for classifying the galaxy as {self.selected}.')
            player.classification_index += 1
            
            
        return classifying
                            
                        
    def load_classification_data(self, player):
        """
        Load user save data or create a new save if it doesn't exist."""                    
        if os.path.exists(self.classification_save_file):
            with open(self.classification_save_file, 'r') as f:
                self.classification_data = json.load(f)
        else:
            self.classification_data = {}
            for names in self.image_files:
                self.classification_data[names[-22:-4]] = 'None'
            self.save_classification_data()
            
            
    def save_classification_data(self):
        """Save the current game state."""
        
        with open(self.classification_save_file, 'w') as file:
            json.dump(self.classification_data, file)