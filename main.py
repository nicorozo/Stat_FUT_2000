import time
import random 
import modules.team_stats as team_stats
from modules.art_intro import intro_art



def is_goal():
    print("Team chance to score")
    return True if random.random() <= 0.5 else False
     
def should_try(team):

    if random.random() <= team['chances']:
        print(f"{team['name']} attempt for goal and...")
        if is_goal():
            print("Goool") 
        else: 
            print(" Failed")
    return

def set_chances(teams):
    teams[0]["chances"] = 0.1 if (teams[0]["attack"] - teams[1]["defense"]) <= 0 else (teams[0]["attack"] - teams[1]["defense"]) 
    teams[1]["chances"] = 0.1 if (teams[1]["attack"] - teams[0]["defense"]) <= 0 else (teams[1]["attack"] - teams[0]["defense"])
    print("Chances set: ",teams)
    
     

def minute_by_minute(teams):

        match_time = 90
        set_chances(teams)
        for i in range(match_time):

            print(f'Time: {i}')

            should_try(teams[0])
            should_try(teams[1])
            # chance of goal

            time.sleep(0.15)

def fut_simulator():

#Intro art display
    intro_art()
#get names and generate stats
    teams = team_stats.team_generator()
    print(teams[0]["name"], " VS ", teams[1]["name"])
#start the game
    minute_by_minute(teams)

    

    


fut_simulator()