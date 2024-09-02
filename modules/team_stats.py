import random

def randomizer(): #test
    return round(random.random(),2)
def get_name():
    name = input()
    if name == '':
        name = "Lazy Name " + str(random.randint(1,300))
    
    return name

def team_generator():
        
        teams = []
        template = {
        "name": '',
        "score": 0,
        "defense": 0,
        "attack": 0,
        }
        
        for t in range(2):
            teams.append(template.copy() if isinstance(template, (list, dict)) else template)  
            print(f"Team {t + 1} name: ")
            
            teams[t]["name"] = get_name()        
            teams[t]["defense"] = randomizer() #randomizer
            teams[t]["attack"] = randomizer() #randomizer
        
        
        return teams



