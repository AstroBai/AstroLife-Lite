import random
import numpy as np
import json
import os

class Player:
    def __init__(self, name='Player', is_human=True):
        self.name = name
        self.is_human = is_human
        self.actions = ['observe', 'research', 'design_telescope', 'apply_funding', 'attend_conference']
        self.src_loc = os.path.dirname(os.path.abspath(__file__))
        self.save_file = os.path.join(self.src_loc, f'../saves/{self.name}.json')
        self.load_save()
        self.funding = self.save_data['funding']
        self.reputation = self.save_data['reputation']
        self.observations = self.save_data['observations']
        self.telescope = self.save_data['telescope']
        self.telescope_n = self.save_data['telescope_n']
        self.achievements = self.save_data['achievements']
        self.credit = self.save_data['credit']
        self.observation_time = self.save_data['observation_time']
        self.score = self.save_data['score']
        self.planet = self.save_data['planet']
        self.stellar = self.save_data['stellar']
        self.galaxy = self.save_data['galaxy']
        self.cosmology = self.save_data['cosmology']
        self.time = self.save_data['time']
        self.classification_index = self.save_data['classification_index']
        self.funding_date = self.save_data['funding_date']

    #==========================================================================================
    # actions
    def observe(self, silence=False):
        result = random.random() * self.telescope
        self.observations += result
        self.funding -= random.gauss(100, 10) * self.telescope
        if not silence:
            print(f"{self.name} completed an observation with result: {result}")

    def research(self, silence=False):
        if not self.observations:
            if not silence:
                print(f"{self.name} has no data for research.")
            return
        result = self.observations
        self.observations = 0
        self.achievements += max(result * random.gauss(1, 0.3), 0)
        self.funding -= random.gauss(100, 10) * result
        if not silence:
            print(f"{self.name}'s research have result: {result}")

    def design_telescope(self, silence=False):
        self.funding -= random.gauss(100, 10) * 10 ** (self.telescope - 1)
        new_efficiency = self.telescope * random.gauss(1.1, 0.1)
        self.telescope = new_efficiency
        if not silence:
            print(f"{self.name} designed a new telescope with efficiency: {new_efficiency}")

    def apply_funding(self, silence=False):
        if self.reputation == 0 or self.achievements == 0:
            if not silence:
                print(f"{self.name} cannot apply for funding with zero reputation or achievements.")
            return
        funding_received = random.gauss(1000, 100) * np.sqrt(self.reputation) * np.sqrt(self.achievements) / self.credit
        self.credit *= 1.1
        self.funding += funding_received
        if not silence:
            print(f"{self.name} received funding: {funding_received}")

    def attend_conference(self, silence=False):
        reputation_received = random.random() * np.sqrt(self.achievements) / self.credit
        self.credit *= 1.1
        self.reputation += reputation_received
        self.funding -= random.gauss(10, 1)
        if not silence:
            print(f"{self.name} received reputation: {reputation_received}")

    #==========================================================================================
    def get_state(self):
        return [self.funding, self.reputation, self.observations, self.telescope, self.achievements, self.credit]

    def _get_reward(self):
        if self.funding <= 0:
            return -np.inf
        return np.log10(self.funding) + self.reputation + self.telescope + self.achievements


    def get_status(self):
        if self.funding <= 0: #or self.reputation <= 0:
            self.score = 0
        else:
            self.score = max(np.log10(self.funding) + self.reputation + self.telescope + self.achievements - 4, 0)
        return [self.name, round(max(0,self.observations), 2), round(self.funding), round(self.reputation, 2), round(self.telescope, 2), round(self.achievements, 2), round(self.score, 2)]

    def update(self, time):
        self.save_data = {"name": self.name, 
                          "time": time,
                              "funding": self.funding,
                              "reputation": self.reputation,
                              "observations": self.observations,
                              "telescope": self.telescope,
                              "telescope_n": self.telescope_n,
                              "achievements": self.achievements,
                              "credit": self.credit,
                              "observation_time": self.observation_time,
                              "score": self.score,
                              "planet": self.planet,
                              "stellar": self.stellar,
                              "galaxy": self.galaxy,
                              "cosmology": self.cosmology,
                              "classification_index": self.classification_index,
                              "funding_date": self.funding_date
                              }
    
    
    def load_save(self):
        """Load user save data or create a new save if it doesn't exist."""
        if not os.path.exists(os.path.join(self.src_loc, '../saves')):
            os.makedirs(os.path.join(self.src_loc, '../saves'))
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as file:
                self.save_data = json.load(file)
        else:
            self.save_data = {"name": self.name, 
                              "time": 0,
                              "funding": 1000,
                              "reputation": 0,
                              "observations": 0,
                              "telescope": 1.0,
                              "telescope_n": 1,
                              "achievements": 0,
                              "credit": 1,
                              "observation_time": 0,
                              "score": 0,
                              "planet": 0,
                              "stellar": 0,
                              "galaxy": 0,
                              "cosmology": 0,
                              "classification_index": 0,
                              "funding_date": 0}  # Default save data
            self.save_game()

    def save_game(self):
        """Save the current game state."""
        
        with open(self.save_file, 'w') as file:
            json.dump(self.save_data, file)