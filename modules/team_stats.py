import random


def randomizer():  # test
    return round(random.random(), 2)


def get_name():
    name = input()
    if name == '':
        name = "Lazy Name " + str(random.randint(1, 300))

    return name


def set_goal_chances(teams):
    teams[0]["chances"] = 0.1 if (
        teams[0]["attack"] - teams[1]["defense"]) <= 0 else round((teams[0]["attack"] - teams[1]["defense"]), 2)
    teams[1]["chances"] = 0.1 if (
        teams[1]["attack"] - teams[0]["defense"]) <= 0 else round((teams[1]["attack"] - teams[0]["defense"]), 2)
    print("Chances set: ", teams)


def team_generator():

    teams = []
    template = {
        "name": '',
        "score": 0,
        "defense": 0,
        "attack": 0,
        "pass_counter": 0
    }

    for t in range(2):
        teams.append(template.copy() if isinstance(
            template, (list, dict)) else template)
        print(f"Team {t + 1} name: ")

        teams[t]["name"] = get_name()
        teams[t]["defense"] = randomizer()  # randomizer
        teams[t]["attack"] = randomizer()  # randomizer

    # adding "chances" to teams
    set_goal_chances(teams)

    return teams
