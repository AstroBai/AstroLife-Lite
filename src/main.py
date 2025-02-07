import pygame
import argparse
from settings import Settings
from pygame_gui import UIManager
from button import Button
from player import Player
import sys
import pygame_gui
from draw import Draw
from manage_observations import ManageObservations
from timesys import Time
from shop import Shop
from research import Research
from learn import Learn
from message import Message
from music import Music
from conference import Conference
from apply_funding import ApplyFunding
from classification import Classification
import os


class Main:
    def __init__(self, username):
        pygame.init()
        src_loc = os.path.dirname(os.path.abspath(__file__))
        pygame.display.set_caption('AstroLife-Lite v0.1')
        icon = pygame.image.load(os.path.join(src_loc,'../assets/images/icon.png'))
        pygame.display.set_icon(icon)
        self.settings = Settings()
        self.settings.set_screen(1280*1.5,800*1.5)      
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.manager = UIManager((self.settings.screen_width, self.settings.screen_height),os.path.join(src_loc,'../data/theme.json'))
        self.clock = pygame.time.Clock()
        
        self.music = Music(self.screen, self.manager, draw_muse=True)
        self.draw = Draw(self.screen, self.manager)
        self.player = Player(username)
        self.button = Button(self.screen, self.manager)

        
        self.message = Message(self.screen, self.manager)
        self.manage_observations = ManageObservations(self.screen, self.manager, self.message)
        self.shop = Shop(self.screen, self.manager, self.message, self.player)
        self.research = Research(self.screen, self.manager, self.message)
        self.learn = Learn(self.screen, self.manager, self.message, self.player)
        self.conference = Conference(self.screen, self.manager, self.message)
        self.applyfunding = ApplyFunding(self.screen, self.manager, self.message, self.player)
        self.classification = Classification(self.screen, self.manager, self.message, self.player)
        
        self.button.hide_all()
        self.shop.create_shop()
        self.shop.hide_all()
        self.research.create_research()
        self.research.hide_all()
        self.research.progress.hide()
        self.learn.create_learn()
        self.learn.hide_all()
        self.learn.progress.hide()
        self.message.hide_all()
        self.conference.create_conference()
        self.conference.hide_all()
        self.applyfunding.create_funding()
        self.applyfunding.hide_all()
        self.classification.create_classification()
        self.classification.hide_all()
        
        self.running_menu = True
        self.running = True
        self.current_screen = 'game_main'
        self.window = 'None'
        
        self.show_manage_observations = False
        self.shopping = False
        self.researching = False
        self.learning = False
        self.show_conference = False
        self.show_classification = False
        self.apply_funding = False
    
    def main_loop(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.timesys = Time(self.screen, self.manager)
        self.timesys.deltat = self.player.time
        self.timesys.Pause()
        self.manage_observations.create_calender(5*((self.timesys.get_day()[0]-1)//5)+1)
        self.manage_observations.hide_all()
        self.message.update(time_delta, self.timesys.get_day(), f'Welcome {self.player.name}!')
        current_music_index = 0
        self.music.play_music(current_music_index)
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            self.timesys.update(time_delta)
            self.date = self.timesys.get_date()
            self.week = self.timesys.get_day()[0]
            self.day = self.timesys.get_day()
            self.player.auto_save()
            self.research.update(time_delta,self.player,self.date,self.day)
            self.learn.update(time_delta,self.player,self.date, self.day)
            self.message.update(time_delta,self.day )
            self.message.show_all()
            self.manage_observations.update(time_delta, self.day, self.player) 
            self.conference.update(time_delta, self.player, self.date, self.day)
            if self.timesys.update_calender():
                self.manage_observations.hide_all_calender_buttons()
                self.manage_observations.create_calender(self.week,only_calender=True)
                self.manage_observations.hide_all_calender_buttons()
                
            
            if self.current_screen == 'game_main':
                self.draw.draw_background()
                self.draw.draw_bg()
                self.draw.draw_frame()
                self.draw.draw_status(self.player)
                self.draw.draw_title(self.player)
                self.timesys.draw_date()
                self.timesys.draw()
                self.button.update(time_delta)
                self.button.show_all()
                self.button.draw()
 
            # Manage Observation
            if self.show_manage_observations and self.window == 'manage_observations':
                self.shop.hide_all()
                self.research.hide_all()
                self.learn.hide_all()
                self.conference.hide_all()
                self.classification.hide_all()
                self.applyfunding.hide_all()
                self.manage_observations.days = self.player.observation_time
                self.manage_observations.draw_calender()
                self.manage_observations.show_all()
                self.manage_observations.draw()
            
            # Shop
            if self.shopping and self.window == 'shop':
                self.manage_observations.hide_all()
                self.research.hide_all()
                self.learn.hide_all()
                self.conference.hide_all()
                self.classification.hide_all()
                self.applyfunding.hide_all()
                self.shop.funding = self.player.funding
                self.shop.draw_shop()
                self.shop.update(time_delta, self.player) 
                self.shop.show_all()
                self.shop.draw()    
                
            # Research
            if self.researching and self.window == 'research':
                self.manage_observations.hide_all()
                self.shop.hide_all()
                self.learn.hide_all()
                self.conference.hide_all()
                self.classification.hide_all()
                self.applyfunding.hide_all()
                self.research.draw_research()
                self.research.show_all()
                self.research.draw()     
                
            # Learn
            if self.learning and self.window == 'learn':
                self.manage_observations.hide_all()
                self.shop.hide_all()
                self.research.hide_all()
                self.conference.hide_all()
                self.classification.hide_all()
                self.applyfunding.hide_all()
                self.learn.draw_learn()
                self.learn.show_all()
                self.learn.draw()       
                
            # Conference
            if self.show_conference and self.window == 'conference':
                self.manage_observations.hide_all()     
                self.shop.hide_all()
                self.research.hide_all()
                self.learn.hide_all()
                self.classification.hide_all()
                self.applyfunding.hide_all()
                self.conference.draw_conference()   
                self.conference.update(time_delta, self.player, self.date, self.day) 
                self.conference.show_all()
                self.conference.draw()    
                
            # Apply Funding
            if self.apply_funding and self.window == 'apply_funding':
                self.manage_observations.hide_all()     
                self.shop.hide_all()
                self.research.hide_all()
                self.learn.hide_all()
                self.conference.hide_all()
                self.classification.hide_all()
                self.applyfunding.draw_funding()   
                self.applyfunding.update(time_delta, self.player, self.date, self.day) 
                self.applyfunding.show_all()
                self.applyfunding.draw()    
            
            # Classification
            if self.show_classification and self.window == 'classification':
                self.manage_observations.hide_all()     
                self.shop.hide_all()
                self.research.hide_all()
                self.learn.hide_all()
                self.conference.hide_all()
                self.applyfunding.hide_all()
                self.classification.draw_classification()   
                self.classification.update(time_delta, self.player) 
                self.classification.show_all()
                self.classification.draw()    
                
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.timesys.Pause() 
                    time = self.timesys.deltat
                    self.player.update(time)
                    self.player.save_game()
                    
                    self.running = False
                    pygame.quit()
                    sys.exit()

                self.manager.process_events(event)
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    self.music.play_click()
                    
                    if event.ui_element == self.button.exit_button:
                        self.timesys.Pause() 
                        time = self.timesys.deltat
                        self.player.update(time)
                        self.player.save_game()
                        self.running = False
                        pygame.quit()
                        sys.exit()
                    
                    # Manage Observation
                    if event.ui_element == self.button.manage_observations: 
                        self.show_manage_observations = True
                        self.window = 'manage_observations'
                    if self.show_manage_observations:
                        self.show_manage_observations = self.manage_observations.manage(event, self.player)
                        
                    # Shop
                    if event.ui_element == self.button.shop:
                        self.shopping = True
                        self.window = 'shop'
                    if self.shopping:
                        self.shopping = self.shop.manage(event,self.player,time_delta,self.day)    
                        
                    # Research    
                    if event.ui_element == self.button.research:
                        self.researching = True
                        self.window = 'research'
                    if self.researching:
                        self.researching = self.research.manage(event,self.player,time_delta,self.day)    
                        
                    # Learn   
                    if event.ui_element == self.button.learn:
                        self.learning = True
                        self.window = 'learn'
                    if self.learning:
                        self.learning = self.learn.manage(event,self.player, time_delta,self.day)       
                        
                    # Conference
                    if event.ui_element ==  self.button.conference:
                        self.show_conference = True
                        self.window = 'conference'
                    if self.show_conference:
                        self.show_conference = self.conference.manage(event,self.player,time_delta, self.date, self.day)   
                        
                    # Apply Funding
                    if event.ui_element == self.button.apply_funding:
                        self.apply_funding = True
                        self.window = 'apply_funding'
                    if self.apply_funding:
                        self.apply_funding = self.applyfunding.manage(event,self.player,time_delta, self.date, self.day)    
                        
                    # Classification
                    if event.ui_element ==  self.button.classification:
                        self.show_classification = True
                        self.window = 'classification'
                    if self.show_classification:
                        self.show_classification = self.classification.manage(event,self.player,time_delta,self.day)    
                           
                
                    
                    if event.ui_element == self.timesys.pause:
                        self.timesys.Pause()    
                    if event.ui_element == self.music.muse_btn:
                        self.music.muse() 
                        
                        
                        
            if not pygame.mixer.music.get_busy():  
                current_music_index = (current_music_index + 1) % len(self.music.music_files) 
                self.music.play_music(current_music_index)            
        
            pygame.display.flip()
            
            
 
def main_entry():
    parser = argparse.ArgumentParser(description="AstroLife Game")
    parser.add_argument('-u', '--username', type=str, default='Player', help='Username for the game')
    args = parser.parse_args()
    
    game = Main(args.username)
    game.main_loop()          
    
    
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AstroLife Game')
    parser.add_argument('-u', '--username', type=str, default='Player', help='Username for the game')
    args = parser.parse_args()
    main = Main(args.username)
    main.main_loop()          
            