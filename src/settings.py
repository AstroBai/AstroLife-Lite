from screeninfo import get_monitors
import os
import json

class Settings:
    def __init__(self):
        self.var_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/vars.json')
        self.load()
        
    def set_screen(self, w=1280, h=800):
        self.screen_width = w
        self.screen_height = h
        self.save()    
        
    def load(self):
        with open(self.var_file, 'r') as file:
            variables = json.load(file)
            self.screen_height = variables['screen_height']
            self.screen_width = variables['screen_width']
        
            
    def save(self):
        data = {
            'screen_width': self.screen_width,
            'screen_height': self.screen_height,
        }
        with open(self.var_file, 'w') as file:
            json.dump(data, file, indent=4)             

    