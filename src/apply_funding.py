import pygame
import pygame_gui
from draw import Draw
import random
import os
import numpy as np

class ApplyFunding:
    def __init__(self, screen, manager, message, player):
        self.screen = screen
        self.manager = manager
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.Draw = Draw(self.screen,self.manager)
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.icon_scale = self.screen.get_height() * 0.05
        self.message = message
        self.application_frame = pygame.image.load(os.path.join(src_loc,'../assets/images/application.png'))
        self.possibility = 0
        self.applied = False
        self.date_end = player.funding_date

        
            
        
        
    def create_funding(self):
        self.application_width = self.application_frame.get_width()
        self.application_height = self.application_frame.get_height()
        self.x_application = self.screen_length/2 - self.application_width/2
        self.y_application = self.screen_height/3 + 20

        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.screen_length/2 - 100, self.screen_height/2 + 320), (200, 50)),
            text='Back',
            manager=self.manager,
            object_id='#button_black'
        )
        
        self.enter_amount = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.x_application + 280, self.y_application + 85), (400, 50)),
            initial_text='10000',
            manager=self.manager
        )
        
        self.select_duration = pygame_gui.elements.UIDropDownMenu(
            options_list=['10 Weeks', '20 Weeks', '40 Weeks', '80 Weeks', '100 Weeks', '200 Weeks'],
            starting_option='10 Weeks',
            relative_rect=pygame.Rect((self.x_application + 280, self.y_application + 140), (400, 50)),
            manager=self.manager
        )
        
        self.sign_box = pygame_gui.elements.UITextEntryLine(    
            relative_rect=pygame.Rect((self.x_application + 280, self.y_application + 275), (400, 50)),
            manager=self.manager
        )
        
        self.confirm = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.x_application + 680, self.y_application + 275), (200, 50)),
            text='Confirm',
            manager=self.manager,
            object_id='#button_black'
        )
        self.info_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((self.x_application+20, self.y_application + 340), (self.application_width-40, 120)),
            html_text=f'<p>Result will be shown here after you confirm the application.</p>',
            manager=self.manager
        )
        
        
        
        
        
        
        
        
    def draw_funding(self):
        # draw frame
        self.application_frame = pygame.transform.scale(self.application_frame, (self.application_width, self.application_height))
        self.screen.blit(self.application_frame, (self.x_application, self.y_application))
        self.Draw.draw_text('Application Form', self.x_application+20, self.y_application+20, (0,0,0),size=48)
        self.Draw.draw_text('Expected Amount ($):', self.x_application+20, self.y_application+100, (0,0,0))
        self.Draw.draw_text('Select Duration:', self.x_application+20, self.y_application+160, (0,0,0))
        self.Draw.draw_text(f'The Success Possibility is {100*self.possibility:.2f}%', self.x_application+20, self.y_application+220, (0,0,0))
        self.Draw.draw_text('Sign to Confirm:', self.x_application+50, self.y_application+290, (0,0,0))
        
                

    def show_all(self):
        self.back_button.show()  
        self.enter_amount.show()
        self.select_duration.show()
        self.sign_box.show()
        self.confirm.show() 
        self.info_box.show()

    
    def draw(self):
        self.manager.draw_ui(self.screen)    
                
                
    def hide_all(self):
        self.back_button.hide()    
        self.enter_amount.hide()    
        self.select_duration.hide()    
        self.sign_box.hide()    
        self.confirm.hide()    
        self.info_box.hide()    



                
    def update(self, time_delta, player, date, day):
        self.manager.update(time_delta)
        if self.enter_amount.get_text() != '':
            self.amount = float(self.enter_amount.get_text())+1e-5   
        else: self.amount = 1e-5
        self.duration = self.select_duration.selected_option[0]
        if self.duration == '10 Weeks':
            self.duration = 10
        elif self.duration == '20 Weeks':
            self.duration = 20
        elif self.duration == '40 Weeks':
            self.duration = 40
        elif self.duration == '80 Weeks':
            self.duration = 80
        elif self.duration == '100 Weeks':
            self.duration = 100
        elif self.duration == '200 Weeks':
            self.duration = 200
        self.possibility = 1 - np.exp(-(player.achievements* (player.reputation+0.1) * self.duration / self.amount))
        
        if self.sign_box.get_text() != player.name or self.applied:
            self.confirm.disable()
        else:
            self.confirm.enable()    
        
        if self.applied and date >= self.date_end:
            self.applied = False   
        
             
           
    def manage(self, event, player, time_delta, date, day):
        event_name = event.ui_element
        funding = True
        if event_name == self.back_button:
            self.hide_all()
            funding = False   
        
        if event_name == self.confirm:
            self.applied = True
            random_num = random.random()
            self.date_end = date + self.duration*7
            player.funding_date = self.date_end
            if random_num < self.possibility:
                player.funding += self.amount
                self.info_box.set_text(f'<p>Congratulations! Your application has been successful. You have been awarded ${self.amount:.2f}. The next funding period will start in {self.duration} weeks.</p>')
                self.message.update(time_delta, day, f'Congratulations! Your application has been successful. You have been awarded ${self.amount:.2f}. The next funding period will start in {self.duration} weeks.')
            else:
                self.info_box.set_text(f'<p>Unfortunately, your application has not been successful. You have not been awarded any funding. The next funding period will start in {self.duration} weeks.</p>')
                self.message.update(time_delta, day, f'Unfortunately, your application has not been successful. You have not been awarded any funding. The next funding period will start in {self.duration} weeks.')
                
                
            
        return funding
                            
    
                        