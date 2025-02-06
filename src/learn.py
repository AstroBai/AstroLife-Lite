import pygame
import matplotlib.pyplot as plt
import numpy as np
import pygame_gui
from draw import Draw
import random
import os

class Learn:
    def __init__(self, screen, manager, message, player):
        self.screen = screen
        self.manager = manager
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.Draw = Draw(self.screen,self.manager)
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.icon_scale = self.screen.get_height() * 0.05
        self.book_frame = pygame.image.load(os.path.join(src_loc,'../assets/images/book.png'))
        self.item_frame = pygame.image.load(os.path.join(src_loc,'../assets/images/goldshade.png'))
        self.planet = pygame.image.load(os.path.join(src_loc,'../assets/images/planet.png'))
        self.stellar = pygame.image.load(os.path.join(src_loc,'../assets/images/stellar.jpg'))
        self.galaxy = pygame.image.load(os.path.join(src_loc,'../assets/images/galaxy.png'))
        self.cosmology = pygame.image.load(os.path.join(src_loc,'../assets/images/cosmology.jpg'))
        self.planet_level = player.planet
        self.stellar_level = player.stellar
        self.galaxy_level = player.galaxy
        self.cosmology_level = player.cosmology
        
        self.planet_level_tmp = player.planet
        self.stellar_level_tmp = player.stellar
        self.galaxy_level_tmp = player.galaxy 
        self.cosmology_level_tmp = player.cosmology
        
        self.planet_price = player.planet + 1
        self.stellar_price = player.stellar + 1
        self.galaxy_price = player.galaxy + 1
        self.cosmology_price = player.cosmology + 1
        
        self.new_learn = True
        self.date_0 = 0
        self.start = False
        self.duration = 1
        
        self.upgrader = None
        self.message = message
        
        self.learnt = None
            
        
        
    def create_learn(self):
        src_loc = os.path.dirname(os.path.abspath(__file__))
        calender = pygame.image.load(os.path.join(src_loc,'../tmp/images/calender.png'))
        self.book_width = calender.get_width()
        self.book_height = calender.get_height()
        self.book_frame = pygame.transform.scale(self.book_frame, (self.book_width, self.book_height))
        self.x_book = self.screen_length/2 - self.book_width/2
        self.y_book = self.screen_height/3 
        item_size = self.screen_height / 8
        
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_book + self.book_width - 170, self.y_book + 480), (90, 45)),
            text='Back',
            manager=self.manager,
            object_id='#button_white'
        )
        
        self.upgrade_planet = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_book + 300, self.y_book + 70), (120, 45)),
            text=f'{self.planet_price} Week',
            manager=self.manager,
            object_id='#button_white'
        )
        
        self.upgrade_stellar = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_book + 300, self.y_book + 70 + self.y_book/2), (120, 45)),
            text=f'{self.stellar_price} Week',
            manager=self.manager,
            object_id='#button_white'
        )
        
        self.upgrade_galaxy = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_book + 300 + self.book_width/2.2, self.y_book + 70), (120, 45)),
            text=f'{self.galaxy_price} Week',
            manager=self.manager,
            object_id='#button_white'
        )
        
        self.upgrade_cosmology = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_book + 300 + self.book_width/2.2, self.y_book + 70 + self.y_book/2), (120, 45)),
            text=f'{self.cosmology_price} Week',
            manager=self.manager,
            object_id='#button_white'
        )
        
        self.progress = pygame_gui.elements.UIProgressBar(
            relative_rect=pygame.Rect((self.x_book + 80, self.y_book - 290), (self.book_width-160, 30)),
            manager=self.manager,
            object_id='#progress_bar_blue'
        )
        
        self.planet_level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.x_book + 300, self.y_book + 150), (120, 30)),
            text=f'Level: {self.planet_level}',
            manager=self.manager,
            object_id='#label_black'
        )
        
        self.stellar_level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.x_book + 300, self.y_book + 150 + self.y_book/2), (120, 30)),
            text=f'Level: {self.stellar_level}',
            manager=self.manager,
            object_id='#label_black'
        )
        
        self.galaxy_level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.x_book + 300 + self.book_width/2.2, self.y_book + 150), (120, 30)),
            text=f'Level: {self.galaxy_level}',
            manager=self.manager,
            object_id='#label_black'
        )
        
        self.cosmology_level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((self.x_book + 300 + self.book_width/2.2, self.y_book + 150 + self.y_book/2), (120, 30)),
            text=f'Level: {self.cosmology_level}',
            manager=self.manager,
            object_id='#label_black'
        )
    
        
        
        
    def draw_learn(self):
        # draw frame
        self.book_frame = pygame.transform.scale(self.book_frame, (self.book_width, self.book_height))
        self.screen.blit(self.book_frame, (self.x_book, self.y_book))
        item_size = self.screen_height / 8
        self.item_frame = pygame.transform.scale(self.item_frame, (item_size,item_size))
        
        # draw items
        x_item_init = self.x_book + 100
        y_item_init = self.y_book + 50
        self.planet = pygame.transform.scale(self.planet, (item_size,item_size))
        self.screen.blit(self.planet, (x_item_init,y_item_init))
        self.screen.blit(self.item_frame, (x_item_init,y_item_init))
        self.Draw.draw_text('Upgrade Planetary Science', x_item_init,y_item_init+ item_size + 10,color=(0,0,0))
        
        self.stellar = pygame.transform.scale(self.stellar, (item_size,item_size))
        self.screen.blit(self.stellar, (x_item_init,y_item_init + self.y_book/2))
        self.screen.blit(self.item_frame, (x_item_init,y_item_init+ self.y_book/2))
        self.Draw.draw_text('Upgrade Stellar Physics', x_item_init,y_item_init+ item_size + 10 + self.y_book/2,color=(0,0,0))

        
        self.galaxy = pygame.transform.scale(self.galaxy, (item_size,item_size))
        self.screen.blit(self.galaxy, (x_item_init + self.book_width/2.2,y_item_init))
        self.screen.blit(self.item_frame, (x_item_init + self.book_width/2.2,y_item_init))
        self.Draw.draw_text('Upgrade Galaxy Astronomy', x_item_init + self.book_width/2.2,y_item_init+ item_size + 10,color=(0,0,0))
        
        self.cosmology = pygame.transform.scale(self.cosmology, (item_size,item_size))
        self.screen.blit(self.cosmology, (x_item_init + self.book_width/2.2,y_item_init + self.y_book/2))
        self.screen.blit(self.item_frame, (x_item_init + self.book_width/2.2,y_item_init+ self.y_book/2))
        self.Draw.draw_text('Upgrade Cosmology', x_item_init + self.book_width/2.2,y_item_init+ item_size + 10 + self.y_book/2,color=(0,0,0))
        
        
        
        
        
          
        
    def show_all(self):
        self.back_button.show()  
        self.upgrade_planet.show()
        self.upgrade_stellar.show()
        self.upgrade_galaxy.show()
        self.upgrade_cosmology.show()
        self.planet_level_label.show()
        self.stellar_level_label.show()
        self.galaxy_level_label.show()
        self.cosmology_level_label.show()

   

    
    def draw(self):
        self.manager.draw_ui(self.screen)    
                
                
    def hide_all(self):
        self.back_button.hide()     
        self.upgrade_planet.hide()
        self.upgrade_stellar.hide()
        self.upgrade_galaxy.hide()
        self.upgrade_cosmology.hide()
        self.planet_level_label.hide()
        self.stellar_level_label.hide()
        self.galaxy_level_label.hide()
        self.cosmology_level_label.hide()

                
    def update(self, time_delta, player, date, day):
        self.progress.hide()
        self.upgrade_planet.enable()
        self.upgrade_stellar.enable()
        self.upgrade_galaxy.enable()
        self.upgrade_cosmology.enable() 
        self.planet_level_label.set_text(f'Level: {self.planet_level}')
        self.stellar_level_label.set_text(f'Level: {self.stellar_level}')
        self.galaxy_level_label.set_text(f'Level: {self.galaxy_level}')
        self.cosmology_level_label.set_text(f'Level: {self.cosmology_level}')
        
        self.upgrade_planet.set_text(f'{self.planet_price} Week')
        self.upgrade_stellar.set_text(f'{self.stellar_price} Week')
        self.upgrade_galaxy.set_text(f'{self.galaxy_price} Week')
        self.upgrade_cosmology.set_text(f'{self.cosmology_price} Week')
        
        self.manager.update(time_delta)  
        if self.new_learn:
            self.progress.hide()
            if self.planet_level == self.stellar_level and self.stellar_level == self.galaxy_level and self.galaxy_level == self.cosmology_level:
                pass
            else: 
                if not self.planet_level < max(self.planet_level,self.stellar_level,self.galaxy_level,self.cosmology_level):
                    self.upgrade_planet.disable()
                if not self.stellar_level < max(self.planet_level,self.stellar_level,self.galaxy_level,self.cosmology_level):
                    self.upgrade_stellar.disable()    
                if not self.galaxy_level < max(self.planet_level,self.stellar_level,self.galaxy_level,self.cosmology_level):
                    self.upgrade_galaxy.disable()     
                if not self.cosmology_level < max(self.planet_level,self.stellar_level,self.galaxy_level,self.cosmology_level):
                    self.upgrade_cosmology.disable() 
        else:
            self.upgrade_planet.disable()
            self.upgrade_stellar.disable()
            self.upgrade_galaxy.disable()
            self.upgrade_cosmology.disable()  
            if self.start == False:
                self.date_0 = date
                self.start = True   
            current_progress =  (date-self.date_0) / self.duration / 7 * 100
            if current_progress <= 100:
                self.progress.set_current_progress(current_progress)    
                self.progress.show()      
            else: 
                self.planet_level = self.planet_level_tmp
                self.stellar_level = self.stellar_level_tmp
                self.galaxy_level = self.galaxy_level_tmp
                self.cosmology_level = self.cosmology_level_tmp
                
                player.planet = self.planet_level_tmp
                player.stellar = self.stellar_level_tmp
                player.galaxy = self.galaxy_level_tmp
                player.cosmology = self.cosmology_level_tmp
                
                self.message.update(time_delta, day, f'You have finished learning {self.learnt}.')
                self.new_learn = True 
                self.start = False
                
                  
                
                   

        
        
        
             
           
    def manage(self, event, player, time_delta, day):

        event_name = event.ui_element
        learning = True
        if event_name == self.back_button:
            self.hide_all()
            learning = False    
        
        if event_name == self.upgrade_planet:
            self.learnt = 'Planetary Science'
            self.duration = self.planet_price
            self.planet_price += 1
            self.new_learn = False
            self.planet_level_tmp += 1
            self.message.update(time_delta, day, f'You started to learn {self.learnt}, which will be finished in {self.planet_price-1} weeks.')
            
        
        if event_name == self.upgrade_stellar:
            self.learnt = 'Stellar Physics'
            self.duration = self.stellar_price
            self.stellar_price += 1 
            self.new_learn = False
            self.stellar_level_tmp += 1
            self.message.update(time_delta, day, f'You started to learn {self.learnt}, which will be finished in {self.stellar_price-1} weeks.')
            
        if event_name == self.upgrade_galaxy:
            self.learnt = 'Galaxy Astronomy'
            self.duration = self.galaxy_price
            self.galaxy_price += 1
            self.new_learn = False    
            self.galaxy_level_tmp += 1
            self.message.update(time_delta, day, f'You started to learn {self.learnt}, which will be finished in {self.galaxy_price-1} weeks.')
            
        if event_name == self.upgrade_cosmology:
            self.learnt = 'Cosmology'
            self.duration = self.cosmology_price
            self.cosmology_price += 1
            self.new_learn = False    
            self.cosmology_level_tmp += 1
            self.message.update(time_delta, day, f'You started to learn {self.learnt}, which will be finished in {self.cosmology_price-1} weeks.')
            
             
        return learning 
                            
    
                        