#"""CSV provided by "https://www.sports-reference.com/sharing.html?utm_source=direct&utm_medium=Share&utm_campaign=ShareTool">
# Baseball-Reference.com: https://www.baseball-reference.com/leagues/majors/2024-standard-batting.shtml?sr&utm_source=direct&utm_medium=Share&utm_campaign=ShareTool#teams_standard_batting">
# View Original Table Generated 11/19/2025.

import csv
import pygame

# Initialize pygame FIRST
pygame.init()

import visual_objects 
#=======

# Set up display dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("MLB Batting Averages 2024")

# Load background 
background = visual_objects.Background('coors_field.jpg', WINDOW_WIDTH, WINDOW_HEIGHT)

running = True
print(__name__)


if __name__ == "__main__":
    print(__name__)
    # Game loop
    while running:
        
        # ----------------------------------------
        # 1. EVENT HANDLING
        # ----------------------------------------
        
        for event in pygame.event.get():
            # Check if user wants to quit
            if event.type == pygame.QUIT:
                running = False
            
         # Draw the background first
        background.display(screen)
        
        for i in range(len(visual_objects.teamList)):
            visual_objects.teamList[i].display(screen)
            visual_objects.teamList[i].display_label(screen)
    
    # Your data visualization code would go here
    
    # Update the display
        pygame.display.flip()
        # ----------------------------------------
        # 3. DRAWING
        # ----------------------------------------
        # Render everything to the screen
        
        # Clear the screen
    #screen.fill(WHITE)
