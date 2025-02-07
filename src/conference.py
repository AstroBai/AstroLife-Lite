import pygame
import pygame_gui
from draw import Draw
import random
import os

class Conference:
    def __init__(self, screen, manager, message):
        self.screen = screen
        self.manager = manager
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.Draw = Draw(self.screen,self.manager)
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.icon_scale = self.screen.get_height() * 0.05
        self.phone_frame = pygame.image.load(os.path.join(src_loc,'../assets/images/phone.png'))
        self.message = message
        self.requirement = 0
        self.charge = 0
        self.time = 0
        self.reward = 0
        self.level = 0
        self.choice = 'Small'
        self.preparing = False
        self.date_end = 0
        self.time_remind = 7
        self.requirement_confirmed = 0

        
            
        
        
    def create_conference(self):
        self.phone_width = self.phone_frame.get_width()/3
        self.phone_height = self.phone_frame.get_height()/3
        self.x_phone = self.screen_length/2 - self.phone_width/2
        self.y_phone = self.screen_height/10
        
        
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.screen_length/2 - 100, self.screen_height/2 + 320), (200, 50)),
            text='Back',
            manager=self.manager,
            object_id='#button_black'
        )
        
        self.conference_size = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect((self.screen_length/2 - 120, self.screen_height/2 - 320 + 100), (300, 50)),
            options_list= ['Small', 'Medium', 'Large'],
            starting_option='Small',
            manager=self.manager,
        )
        
        self.select_field = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect((self.screen_length/2 - 120, self.screen_height/2 - 270 + 100), (300, 50)),
            options_list = ['Planetary Science', 'Stellar Physics', 'Galaxy Astronomy', 'Cosmology'],
            starting_option= 'Planetary Science',
            manager=self.manager,
        )
        
        self.info_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((self.screen_length/2 - 200, self.screen_height/2 - 200 + 100), (400, 300)),
            html_text=f'<p>Require: </p><p>{self.requirement} Achievements</p><p>Charging ${self.charge}</p><p>Complete in {self.time} Weeks</p><p>{self.level} Levels in {self.select_field.selected_option[1]}</p>',
            manager=self.manager
        )
        
        self.sign_box = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.screen_length/2 , self.screen_height/2 + 100 + 100), (200, 50)),
            manager=self.manager
        )
        
        self.confirm = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.screen_length/2 - 200, self.screen_height/2 + 160 + 100), (400, 50)),     
            text='Confirm',
            manager=self.manager,
            object_id='#button_black'
        )
        
        
        
        
        
        
        
    def draw_conference(self):
        # draw frame
        self.phone_frame = pygame.transform.scale(self.phone_frame, (self.phone_width, self.phone_height*0.9))
        self.screen.blit(self.phone_frame, (self.x_phone, self.y_phone + 100))
        self.Draw.draw_text('Size:', self.screen_length/2 - 200, self.screen_height/2 - 310 + 100, (0,0,0))
        self.Draw.draw_text('Field:', self.screen_length/2 - 200, self.screen_height/2 - 260 + 100, (0,0,0))
        self.Draw.draw_text('Select Your Conference', self.screen_length/2 - 200, self.screen_height/2 - 360 + 100, (0,0,0))
        self.Draw.draw_text('Sign to Confirm: ', self.screen_length/2 - 200, self.screen_height/2 + 120 + 100, (0,0,0))
        
        
        
        
        
          
        
    def show_all(self):
        self.back_button.show()  
        self.conference_size.show()
        self.select_field.show()
        self.info_box.show()
        self.sign_box.show()
        self.confirm.show()
    
    def draw(self):
        self.manager.draw_ui(self.screen)    
                
                
    def hide_all(self):
        self.back_button.hide()     
        self.conference_size.hide()
        self.select_field.hide()
        self.info_box.hide()
        self.sign_box.hide()
        self.confirm.hide()


                
    def update(self, time_delta, player, date, day):
        self.manager.update(time_delta)
        if self.preparing or self.sign_box.text != player.name:
            self.confirm.disable()
        else:
            self.confirm.enable()
        
        self.choice = self.conference_size.selected_option[1]
        if self.choice == 'Small':
            self.requirement = player.achievements + 10
            self.charge = 100
            self.time = 10
            self.level = 2
        elif self.choice == 'Medium':
            self.requirement = player.achievements + 20
            self.charge = 200
            self.time = 15
            self.level = 4
        elif self.choice == 'Large':
            self.requirement = player.achievements + 50
            self.charge = 400
            self.time = 20
            self.level = 8
        self.requirement = round(self.requirement,2)    
        self.info_box.set_text(f'<p>Require: </p><p>{self.requirement} Achievements</p><p>Charging ${self.charge}</p><p>Complete in {self.time} Weeks</p><p>{self.level} Levels in {self.select_field.selected_option[1]}</p>')
        if self.preparing:
            if date >= self.date_end:
                self.time_remind = 7
                self.preparing = False
                self.selected_field = self.select_field.selected_option[1]
                if self.selected_field == 'Planetary Science':
                    self.current_level = player.planet
                elif self.selected_field == 'Stellar Physics':
                    self.current_level = player.stellar
                elif self.selected_field == 'Galaxy Astronomy':
                    self.current_level = player.galaxy
                elif self.selected_field == 'Cosmology':
                    self.current_level = player.comsology
                if player.achievements >= self.requirement_confirmed and self.current_level >= self.level:
                    self.reward = self.level * random.random() + player.achievements - self.requirement_confirmed
                    player.reputation += self.reward
                    self.message.update(time_delta, day, f'Congratulations! You have earned {self.reward} reputation points for attending {self.select_field.selected_option[1]} Conference.')
                else:
                    self.message.update(time_delta, day, f'Sorry, you have not met the requirements to attend {self.select_field.selected_option[1]} Conference.')  
            elif self.time*7 - (self.date_end - date) >= self.time_remind:
                self.message.update(time_delta, day, f'You have {int(self.time - self.time_remind/7)} weeks left to attend {self.select_field.selected_option[1]} Conference. Your target achievements is {self.requirement_confirmed}.')
                self.time_remind += 7
             
           
    def manage(self, event, player, time_delta, date, day):
        event_name = event.ui_element
        conference = True
        if event_name == self.back_button:
            self.hide_all()
            conference = False   
            
        if event_name == self.confirm:
            self.preparing = True
            player.funding -= self.charge
            self.message.update(time_delta, day, f'Start preparing for {self.select_field.selected_option[1]} Conference in {self.time} weeks.')
            self.date_end = date + self.time*7
            self.requirement_confirmed = self.requirement
            
        return conference
                            
    
                        