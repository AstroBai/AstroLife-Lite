import pygame
import matplotlib.pyplot as plt
import numpy as np
import pygame_gui
from draw import Draw
import random
import os

class Shop:
    def __init__(self, screen, manager, message, player):
        self.screen = screen
        self.manager = manager
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.Draw = Draw(self.screen,self.manager)
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.icon_scale = self.screen.get_height() * 0.05
        self.shade = pygame.image.load(os.path.join(src_loc,'../assets/images/redshade.png'))
        self.shop_frame = pygame.image.load(os.path.join(src_loc,'../assets/images/frame2.png'))
        self.observation_time = pygame.image.load(os.path.join(src_loc,'../assets/images/observationtime.png'))
        self.telescope1 = pygame.image.load(os.path.join(src_loc,'../assets/images/telescope.png'))
        self.hst = pygame.image.load(os.path.join(src_loc,'../assets/images/hst.png'))
        self.jwst = pygame.image.load(os.path.join(src_loc,'../assets/images/jwst.png'))
        self.lamost = pygame.image.load(os.path.join(src_loc,'../assets/images/lamost.png'))
        self.desi = pygame.image.load(os.path.join(src_loc,'../assets/images/desi.png'))
        self.lsst = pygame.image.load(os.path.join(src_loc,'../assets/images/lsst.jpg'))
        self.euclid = pygame.image.load(os.path.join(src_loc,'../assets/images/euclid.png'))
        #self.csst = pygame.image.load(os.path.join(src_loc,'../assets/images/csst.png'))
        self.money_bag = pygame.image.load(os.path.join(src_loc,'../assets/images/funding.png'))
        self.money_bag = pygame.transform.scale(self.money_bag, (32,32))
        
        self.upgrade_price = 2**player.telescope_n * 100
        self.funding = player.funding
        self.message = message
        
        
        
            
        
        
    def create_shop(self, only_shop=False):
        src_loc = os.path.dirname(os.path.abspath(__file__))
        calender = pygame.image.load(os.path.join(src_loc,'../tmp/images/calender.png'))
        self.shop = pygame.image.load(os.path.join(src_loc,'../assets/images/bgshop.jpg'))
        self.shop_width = calender.get_width()
        self.shop_height = calender.get_height() + 150
        self.shop = pygame.transform.scale(self.shop, (self.shop_width, self.shop_height))
        self.x_shop = self.screen_length/2 - self.shop_width/2
        self.y_shop = self.screen_height/3 - 100
        
        
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_shop + self.shop_width - 240, self.y_shop + self.shop_height - 130), (90, 45)),
            text='Back',
            manager=self.manager,
            object_id='#button_white'
        )
        # draw item frame
        item_frame_size = self.screen_height / 5
        # draw items
        item_size = self.screen_height / 8
        self.observation_time_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_shop + 140 + item_frame_size*0.1, self.y_shop + 100 + item_frame_size*0.1+ item_size), (item_size, 50)),
            text='$50/Night',
            manager=self.manager
            #object_id='#button_black'
        )
        self.upgrade_telescope = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_shop + 140 + item_frame_size*0.8, self.y_shop + 100 + item_frame_size*0.1+ item_size), (item_size, 50)),
            text=f'${self.upgrade_price}',
            manager=self.manager
            #object_id='#button_black'
        )
        self.hst_price = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_shop + 140 + item_frame_size*1.5, self.y_shop + 100 + item_frame_size*0.1+ item_size), (item_size, 50)),
            text='$10000',
            manager=self.manager
            #object_id='#button_black'
        )
        self.jwst_price = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_shop + 140 + item_frame_size*2.2, self.y_shop + 100 + item_frame_size*0.1+ item_size), (item_size, 50)),
            text='$100000',
            manager=self.manager
            #object_id='#button_black'
        )
        self.lamost_price = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_shop + 140 + item_frame_size*0.1, self.y_shop + 100 + item_frame_size*1.1+ item_size), (item_size, 50)),
            text='$50000',
            manager=self.manager
            #object_id='#button_black'
        )
        self.desi_price = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_shop + 140 + item_frame_size*0.8, self.y_shop + 100 + item_frame_size*1.1+ item_size), (item_size, 50)),
            text='$200000',
            manager=self.manager
            #object_id='#button_black'
        )
        self.lsst_price = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_shop + 140 + item_frame_size*1.5, self.y_shop + 100 + item_frame_size*1.1+ item_size), (item_size, 50)),
            text='$200000',
            manager=self.manager
            #object_id='#button_black'
        )
        self.euclid_price = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_shop + 140 + item_frame_size*2.2, self.y_shop + 100 + item_frame_size*1.1+ item_size), (item_size, 50)),
            text='$200000',
            manager=self.manager
            #object_id='#button_black'
        )
        
        if not only_shop:
            self.funding_number_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((self.x_shop + 200, self.y_shop + self.shop_height - 175), (90, 90)),
                text=f'{self.funding}',
                manager=self.manager,
                object_id='label'
            )
        
    def draw_shop(self):
        self.screen.blit(self.shop, (self.x_shop, self.y_shop))
        # draw frame
        self.shop_frame = pygame.transform.scale(self.shop_frame, (self.shop_width, self.shop_height))
        self.screen.blit(self.shop_frame, (self.x_shop, self.y_shop))
        # draw item frame
        item_frame_size = self.screen_height / 5
        # draw items
        item_size = self.screen_height / 8
        self.shade = pygame.transform.scale(self.shade, (item_size,item_size))
        
        self.Draw.draw_text('Obs. Time',self.x_shop + 140 + item_frame_size*0.15, self.y_shop + 70 + item_frame_size*0.1)
        self.observation_time = pygame.transform.scale(self.observation_time, (item_size,item_size))
        self.screen.blit(self.observation_time, (self.x_shop + 140 + item_frame_size*0.1, self.y_shop + 100 + item_frame_size*0.1))
        self.screen.blit(self.shade, (self.x_shop + 140 + item_frame_size*0.1, self.y_shop + 100 + item_frame_size*0.1))
        
        self.Draw.draw_text('Upgrade Tel.',self.x_shop + 140 + item_frame_size*0.85, self.y_shop + 70 + item_frame_size*0.1)
        self.telescope1 = pygame.transform.scale(self.telescope1, (item_size,item_size))
        self.screen.blit(self.telescope1, (self.x_shop + 140 + item_frame_size*0.8, self.y_shop + 100 + item_frame_size*0.1))
        self.screen.blit(self.shade, (self.x_shop + 140 + item_frame_size*0.8, self.y_shop + 100 + item_frame_size*0.1))
        
        self.Draw.draw_text('H.S.T.',self.x_shop + 140 + item_frame_size*1.55, self.y_shop + 70 + item_frame_size*0.1)
        self.hst = pygame.transform.scale(self.hst, (item_size,item_size))
        self.screen.blit(self.hst, (self.x_shop + 140 + item_frame_size*1.5, self.y_shop + 100 + item_frame_size*0.1))
        self.screen.blit(self.shade, (self.x_shop + 140 + item_frame_size*1.5, self.y_shop + 100 + item_frame_size*0.1))
        
        self.Draw.draw_text('J.W.S.T.',self.x_shop + 140 + item_frame_size*2.25, self.y_shop + 70 + item_frame_size*0.1)
        self.jwst = pygame.transform.scale(self.jwst, (item_size,item_size))
        self.screen.blit(self.jwst, (self.x_shop + 140 + item_frame_size*2.2, self.y_shop + 100 + item_frame_size*0.1))
        self.screen.blit(self.shade, (self.x_shop + 140 + item_frame_size*2.2, self.y_shop + 100 + item_frame_size*0.1))
        
        self.Draw.draw_text('LAMOST',self.x_shop + 140 + item_frame_size*0.15, self.y_shop + 70 + item_frame_size*1.1)
        self.lamost = pygame.transform.scale(self.lamost, (item_size,item_size))
        self.screen.blit(self.lamost, (self.x_shop + 140 + item_frame_size*0.1, self.y_shop + 100 + item_frame_size*1.1))
        self.screen.blit(self.shade, (self.x_shop + 140 + item_frame_size*0.1, self.y_shop + 100 + item_frame_size*1.1))
        
        self.Draw.draw_text('D.E.S.I.',self.x_shop + 140 + item_frame_size*0.85, self.y_shop + 70 + item_frame_size*1.1)
        self.desi = pygame.transform.scale(self.desi, (item_size,item_size))
        self.screen.blit(self.desi, (self.x_shop + 140 + item_frame_size*0.8, self.y_shop + 100 + item_frame_size*1.1))
        self.screen.blit(self.shade, (self.x_shop + 140 + item_frame_size*0.8, self.y_shop + 100 + item_frame_size*1.1))
        
        self.Draw.draw_text('L.S.S.T.',self.x_shop + 140 + item_frame_size*1.55, self.y_shop + 70 + item_frame_size*1.1)
        self.lsst = pygame.transform.scale(self.lsst, (item_size,item_size))
        self.screen.blit(self.lsst, (self.x_shop + 140 + item_frame_size*1.5, self.y_shop + 100 + item_frame_size*1.1))
        self.screen.blit(self.shade, (self.x_shop + 140 + item_frame_size*1.5, self.y_shop + 100 + item_frame_size*1.1))
        
        self.Draw.draw_text('Euclid',self.x_shop + 140 + item_frame_size*2.25, self.y_shop + 70 + item_frame_size*1.1)
        self.euclid = pygame.transform.scale(self.euclid, (item_size,item_size))
        self.screen.blit(self.euclid, (self.x_shop + 140 + item_frame_size*2.2, self.y_shop + 100 + item_frame_size*1.1))
        self.screen.blit(self.shade, (self.x_shop + 140 + item_frame_size*2.2, self.y_shop + 100 + item_frame_size*1.1))
        
        """self.csst = pygame.transform.scale(self.csst, (item_size,item_size))
        self.screen.blit(self.csst, (self.x_shop + 140 + item_frame_size*2.2, self.y_shop + 100 + item_frame_size*1.1))
        self.screen.blit(self.shade, (self.x_shop + 140 + item_frame_size*2.2, self.y_shop + 100 + item_frame_size*1.1))"""
        
        # draw funding
        self.screen.blit(self.money_bag, (self.x_shop + 180, self.y_shop + self.shop_height - 150)) 
        
        
        
        
          
        
    def show_all(self):
        self.back_button.show()     
        self.observation_time_button.show()  
        self.upgrade_telescope.show()
        self.hst_price.show()
        self.jwst_price.show()
        self.lamost_price.show()
        self.desi_price.show()
        self.lsst_price.show()
        self.euclid_price.show()      
        self.funding_number_label.show()

    
    def draw(self):
        self.manager.draw_ui(self.screen)    
                
                
    def hide_all(self):
        self.back_button.hide()     
        self.observation_time_button.hide()  
        self.upgrade_telescope.hide()
        self.hst_price.hide()
        self.jwst_price.hide()
        self.lamost_price.hide()
        self.desi_price.hide()
        self.lsst_price.hide()
        self.euclid_price.hide() 
        self.funding_number_label.hide()
                
    def update(self, time_delta, player):
        self.manager.update(time_delta)    
        self.upgrade_telescope.set_text(f'${self.upgrade_price}')
        self.funding_number_label.set_text(f'{self.funding}')
        
        self.observation_time_button.enable()  
        self.upgrade_telescope.enable()
        self.hst_price.enable()
        self.jwst_price.enable()
        self.lamost_price.enable()
        self.desi_price.enable()
        self.lsst_price.enable()
        self.euclid_price.enable() 
        self.funding_number_label.enable()
        
        if player.funding < 50:
            self.observation_time_button.disable()  
        if player.funding < self.upgrade_price:    
            self.upgrade_telescope.disable()
        if player.funding < 10000:     
            self.hst_price.disable()
        if player.funding < 100000:        
            self.jwst_price.disable()
        if player.funding < 50000:        
            self.lamost_price.disable()
        if player.funding < 200000:        
            self.desi_price.disable()
        if player.funding < 200000:              
            self.lsst_price.disable()
        if player.funding < 200000:      
            self.euclid_price.disable() 
            
        
             
           
    def manage(self, event, player, time_delta, day):
        event_name = event.ui_element
        shopping = True
        if event_name == self.back_button:
            self.hide_all()
            shopping = False
            
        if event_name == self.observation_time_button:
            if player.funding >= 50:
                player.funding -= 50
                player.observation_time += 1
                self.message.update(time_delta, day, 'You spent $50 for 1 night of observation.')
                
        if event_name == self.upgrade_telescope:
            if player.funding >= self.upgrade_price:
                player.funding -= self.upgrade_price
                player.telescope = player.telescope * random.gauss(1.2, 0.05)  
                player.telescope_n += 1
                self.upgrade_price = self.upgrade_price * 2 
                self.message.update(time_delta, day, f'You spent ${self.upgrade_price} to upgrade the telescope.')
        
                     
            
        return shopping 
                            
    
                        