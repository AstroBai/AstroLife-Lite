import pygame
import os
import pygame_gui
from draw import Draw
class Music:
    def __init__(self,screen,manager,draw_muse = False):
        self.screen = screen
        self.manager = manager
        src_loc = os.path.dirname(os.path.abspath(__file__))
        self.music_files = [os.path.join(src_loc,os.path.join(src_loc,f'../assets/sounds/{i}.mp3')) for i in range(7)]
        self.click_file = os.path.join(src_loc,os.path.join(src_loc,f'../assets/sounds/click.wav'))
        self.click_sound = pygame.mixer.Sound(self.click_file)
        self.bell_file = os.path.join(src_loc,os.path.join(src_loc,f'../assets/sounds/bell.wav'))
        self.bell_sound = pygame.mixer.Sound(self.bell_file)
        self.Draw = Draw(self.screen, self.manager)
        self.mixer_music = pygame.mixer.music
        
        h_button = 60
        self.button_scale = self.screen.get_width() * 0.2
        self.icon_scale = self.screen.get_height() * 0.05
        self.center_space_x = self.screen.get_width() * 0.8
        self.Draw = Draw(self.screen, self.manager)
        self.panel_height = self.Draw.panel_height
        self.button_scale_new = self.button_scale - self.panel_height - self.screen.get_width() * 0.02
        if draw_muse:
            self.muse_btn = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((240, 17), (self.button_scale_new*0.4, h_button*0.7)),
                text='Muse',
                manager=self.manager,
                object_id='#button_calender'
            )
        self.mused = False
        
    def play_music(self, index):
        if not self.mused:
            self.mixer_music.load(self.music_files[index])  
            self.mixer_music.set_volume(0.3)
            self.mixer_music.play() 
        
    def play_click(self):
        if not self.mused:
            self.click_sound.play()
        
    def play_bell(self):    
        if not self.mused:  
            self.bell_sound.play()
        
    def muse(self):
        self.mused = not self.mused
        if self.mused:
            self.muse_btn.set_text('Unmuse')
            self.mixer_music.pause()
        else:
            self.muse_btn.set_text('Muse')
            self.mixer_music.unpause()
        
        