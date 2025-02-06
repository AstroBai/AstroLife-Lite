import pygame
import matplotlib.pyplot as plt
import numpy as np
import pygame_gui
from draw import Draw
import random
import os

class Research:
    def __init__(self, screen, manager, message):
        self.screen = screen
        self.manager = manager
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.Draw = Draw(self.screen,self.manager)
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.icon_scale = self.screen.get_height() * 0.05
        self.computer_frame = pygame.image.load(os.path.join(src_loc,'../assets/images/computer.png'))
        self.new_research = True
        self.duration = 0
        self.start = False
        self.date_0 = 0
        self.observation_num = 0
        self.observation_num_label = 0
        self.journal = None
        self.impact = 0
        self.accepted = False
        self.fee = 0
        self.field = None
        self.capable = False
        self.message = message
        
        
            
        
        
    def create_research(self):
        src_loc = os.path.dirname(os.path.abspath(__file__))
        calender = pygame.image.load(os.path.join(src_loc,'../tmp/images/calender.png'))
        self.computer_width = calender.get_width()
        self.computer_height = calender.get_height() + 300
        self.computer_frame = pygame.transform.scale(self.computer_frame, (self.computer_width, self.computer_height))
        self.x_computer = self.screen_length/2 - self.computer_width/2
        self.y_computer = self.screen_height/3 - 200
        
        
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_computer + self.computer_width - 170, self.y_computer + 560), (90, 45)),
            text='Back',
            manager=self.manager,
            object_id='#button_white'
        )
        
        # field
        self.select_field_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((self.x_computer + 60, self.y_computer + 160), (300, 45)),
                text='Select a Field',
                manager=self.manager,
                object_id='label'
            )
        
        self.select_field = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect((self.x_computer + 360, self.y_computer + 160), (300, 45)),
            options_list = ['Planetary Science', 'Stellar Physics', 'Galaxy Astronomy', 'Cosmology'],
            starting_option= 'Planetary Science',
            manager=self.manager
        )
        
        # usage
        self.use_observations_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((self.x_computer + 60, self.y_computer + 220), (300, 45)),
                text='Observation Usage',
                manager=self.manager,
                object_id='label'
            )
        
        self.use_observations = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((self.x_computer + 360, self.y_computer + 220), (300, 45)),
            start_value=0,
            value_range=(0,100), # 
            manager=self.manager
        )
        
        self.use_observations_num_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((self.x_computer + 540, self.y_computer + 220), (300, 45)),
                text=f'{round(self.observation_num,2)}',
                manager=self.manager,
                object_id='label'
            )
        
        # journal
        self.select_journal_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((self.x_computer + 60, self.y_computer + 280), (300, 45)),
                text='Select a Journal',
                manager=self.manager,
                object_id='label'
            )
        
        self.select_journal = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect((self.x_computer + 360, self.y_computer + 280), (450, 45)),
            options_list = ['Research in A&A', 'Astrophysical Journal', 'Nature Astronomy', 'Annual Review of A&A'],
            starting_option= 'Astrophysical Journal',
            manager=self.manager
        )
        
        # info box
        self.info_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((self.x_computer + 80, self.y_computer + 360), (self.computer_width-160, 180)),
            html_text='<p>Information:</p><p>        You are now creating a new research project, which will be finished in around 5 weeks. During this period, you will not be allowed to create any additional research  projects. So please do make sure this is what you want.</p><p>        The charge of your research is $5 per day, and you must pay the publication fee if your research work is accepted. You can monitor the progress of your on-going research in the main screen.</p><p>        If you are sure about all things above, please enter your name in the box below.</p>',
            manager=self.manager
        )
        
        self.sign_box = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.x_computer + 80, self.y_computer + 560), (300, 45)),
            manager=self.manager
        )
        
        self.confirm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_computer + 380, self.y_computer + 560), (150, 45)),
            text='Confirm',
            manager=self.manager,
            object_id='#button_white',
        )
        
        self.progress = pygame_gui.elements.UIProgressBar(
            relative_rect=pygame.Rect((self.x_computer + 80, self.y_computer - 120), (self.computer_width-160, 30)),
            manager=self.manager,
        )
        
        
        
    def draw_research(self):
        # draw frame
        self.computer_frame = pygame.transform.scale(self.computer_frame, (self.computer_width, self.computer_height))
        self.screen.blit(self.computer_frame, (self.x_computer, self.y_computer))
        
        
        
        
          
        
    def show_all(self):
        self.back_button.show()  
        self.select_field_label.show()   
        self.select_field.show()
        self.use_observations_label.show()
        self.use_observations.show()
        self.use_observations_num_label.show()
        self.select_journal_label.show()   
        self.select_journal.show()
        self.info_box.show()
        self.sign_box.show()
        self.confirm_button.show()

    
    def draw(self):
        self.manager.draw_ui(self.screen)    
                
                
    def hide_all(self):
        self.back_button.hide()     
        self.select_field_label.hide()
        self.select_field.hide()
        self.use_observations_label.hide()
        self.use_observations.hide()
        self.use_observations_num_label.hide()
        self.select_journal_label.hide()   
        self.select_journal.hide()
        self.info_box.hide()
        self.sign_box.hide()
        self.confirm_button.hide()
                
    def update(self, time_delta, player, date, day):
        self.manager.update(time_delta)  
        self.observations = player.observations
        self.observation_num_label = self.use_observations.current_value*self.observations/100
        self.use_observations_num_label.set_text(f'{round(self.observation_num_label,2)}') 
        if self.field == 'Planetary Science': self.capable = (player.planet > 0) 
        elif self.field == 'Stellar Physics': self.capable = (player.stellar > 0) 
        elif self.field == 'Galaxy Astronomy': self.capable = (player.stellar > 0) 
        elif self.field == 'Cosmology': self.capable = (player.staller > 0) 
        
        if self.observation_num_label == 0 or not self.sign_box.text == player.name or not self.new_research or not self.capable:
            self.confirm_button.disable()
        else: self.confirm_button.enable()
        
        if self.new_research == False:
            if self.start == False:
                self.date_0 = date
                self.start = True   
            current_progress =  (date-self.date_0) / self.duration * 100
            if current_progress <= 100:
                self.accepted = False
                self.progress.set_current_progress(current_progress)    
                self.progress.show()    
            else: 
                if self.field == 'Planetary Science': sigma = 1/player.planet 
                elif self.field == 'Stellar Physics': sigma = 1/player.stellar 
                elif self.field == 'Galaxy Astronomy': sigma = 1/player.galaxy 
                elif self.field == 'Cosmology': sigma = 1/player.cosmology  
                ratio = random.gauss(1+0.05/sigma, sigma)
                self.outcome = max(0, self.observation_num * ratio)
                if self.journal == 'Research in A&A': 
                    if ratio >= 0.3:
                        self.accepted = True
                        self.impact = 1
                        self.fee = 50
                    else:   
                        self.accepted = False
                        self.impact = 0 
                        self.fee = 0
                elif self.journal == 'Astrophysical Journal':
                    if ratio >= 0.5:
                        self.accepted = True
                        self.impact = 5
                        self.fee = 100
                    else:   
                        self.accepted = False
                        self.impact = 0    
                        self.fee = 0 
                elif self.journal == 'Nature Astronomy': 
                    if ratio >= 1:
                        self.accepted = True
                        self.impact = 10
                        self.fee = 200
                    else:   
                        self.accepted = False
                        self.impact = 0  
                        self.fee = 0   
                elif self.journal == 'Annual Review of A&A': 
                    if ratio >= 1.3:
                        self.accepted = True
                        self.impact = 50     
                        self.fee = 500 
                    else:   
                        self.accepted = False
                        self.impact = 0    
                        self.fee = 0  
                         
                self.new_research = True     
                self.start = False
                self.outcome = self.outcome * self.impact
                player.achievements += self.outcome
                
                player.funding -= self.fee
                player.funding -= 5 * self.duration
                total_charge = int(self.fee + 5 * self.duration)
                if self.accepted:
                    self.message.update(time_delta, day, f'Congrats! Your research work in {self.field} has been accepted by {self.journal}! You are charged ${total_charge} in total. This work helped you earn {round(self.outcome,2)} achievements!')
                else:
                    self.message.update(time_delta, day, f'Sorry, your research work in {self.field} has been rejected by {self.journal}. You are charged ${total_charge} in total.')
                       
                    
        else: 
            self.progress.hide()
        
        
             
           
    def manage(self, event, player, time_delta, day):
        event_name = event.ui_element
        researching = True
        self.journal = self.select_journal.selected_option[1]
        self.field = self.select_field.selected_option[1]
        if event_name == self.back_button:
            self.hide_all()
            researching = False 
        if event_name == self.confirm_button:
            self.hide_all()
            researching = False
            self.new_research = False    
            self.duration = int(random.gauss(35, 2))
            self.observation_num = self.use_observations.current_value*self.observations/100
            player.observations -= self.observation_num
            self.message.update(time_delta, day, f'Your research in {self.field} has started, the work will be submitted to {self.journal}, and the project will be finished in {self.duration} days.')
            
            
        return researching 
                            
    
                        