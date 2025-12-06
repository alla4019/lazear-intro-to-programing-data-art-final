"""
This file creates classes that will draw pygame objects based on imported csv data
MLBteam2024_stats.csv is required to run this code.
"""
import pygame
import csv

# Initialize pygame FIRST
pygame.init()

# Define the images
national_league_img = pygame.image.load("8bit_baseball.png")
american_league_img = pygame.image.load("AmericanLeague8bitbaseball.png")
#=======
# DATA FROM FILE 
#=======
team = []
batting_average = []

with open('MLBteam2024_stats.csv', newline='') as csvfile:
    file = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(file) # skip the header row
    for row in file:
       # print(', '.join(row))
        team.append(row[0]) # list of team names
        batting_average.append(float(row[17])) # list of team batting avgs

class Background:
    """background display"""
    def __init__(self,filename, width, height): 
        self.img = pygame.image.load(filename) 
        self.img = pygame.transform.scale(self.img, (width, height))

    def display(self, screen):
         screen.blit(self.img, (0, 0))  

class Team: 
    """Team class for displaying MLB team batting averages"""
    
    def __init__(self, league_num, idx=0):
        self.x = idx * 50 + 10  # pulling x location from team
        self.y = 500 - (batting_average[idx] * 1000)  # set y position as batting average
        self.name = team[idx]  # string that has team name
        self.font = pygame.font.Font(None, 15)
        
        # Load different image based on league
        if league_num == 1:
            self.img = national_league_img  # Use pre-loaded image
        else:
            self.img = american_league_img
    
    def display(self, screen):
        """Draw the team's baseball image at its position"""
        screen.blit(self.img, (self.x, self.y))
    
    def display_label(self, screen):
        """Adds label beneath team"""
        label_text = f"{self.name}"  # labels team name
        text_surface = self.font.render(label_text, True, (255, 255, 255))
        screen.blit(text_surface, (self.x, self.y + 50))

#list creation
teamList = [Team(league_num=1,idx=0),
Team(league_num=0,idx=1),
Team(league_num=0,idx=2),
Team(league_num=0,idx=3),
Team(league_num=1,idx=4),
Team(league_num=0,idx=5),
Team(league_num=1,idx=6),
Team(league_num=0,idx=7),
Team(league_num=1,idx=8),
Team(league_num=0,idx=9),
Team(league_num=0,idx=10),
Team(league_num=0,idx=11),
Team(league_num=0,idx=12),
Team(league_num=1,idx=13),
Team(league_num=1,idx=14),
Team(league_num=1,idx=15),
Team(league_num=0,idx=16),
Team(league_num=1,idx=17),
Team(league_num=0,idx=18),
Team(league_num=0,idx=19),
Team(league_num=1,idx=20),
Team(league_num=1,idx=21),
Team(league_num=1,idx=22),
Team(league_num=0,idx=23),
Team(league_num=0,idx=24),
Team(league_num=0,idx=25),
Team(league_num=0,idx=26),
Team(league_num=1,idx=27),
Team(league_num=1,idx=28),
Team(league_num=1,idx=29),
Team(league_num=1,idx=30)]