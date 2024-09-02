import time
import random
import modules.team_stats as team_stats
import modules.art_intro as display


def starts_with_ball(teams):
    return teams[random.randint(0, 1)]


def ball_change_team(has_ball, teams):
    if has_ball["name"] == teams[0]["name"]:
        return teams[1]
    else:
        return teams[0]


def something_happens():
    if random.random() <= 0.3:
        return True
    else:
        return False


def is_pass(has_ball):
    has_ball = has_ball["name"]
    # change to team probalities
    if random.random() <= 0.3:
        print(has_ball, " successfull pass")
        # pass +1
        return True
    else:
        print(has_ball, " lost the ball")
        return False


def goal(team_with_ball):
    # add +1 to team score
    team_with_ball["score"] += 1
    # display GOOOAL!
    display.display_goal()
    time.sleep(0.3)

    return


def pass_counter_plus(team_with_ball):
    team_with_ball["pass_counter"] += 1
    return


def minute_by_minute(teams, team_with_ball):

    match_time = 90

    for i in range(match_time):

        print(f'Time: {i}')

        # something happens?
        if something_happens():
            if is_pass(team_with_ball):
                # pass +1 and check for goal
                pass_counter_plus(team_with_ball)
                if team_with_ball["pass_counter"] == 3:
                    goal(team_with_ball)
                    team_with_ball["pass_counter"] = 0
                    ball_change_team(team_with_ball, teams)
            else:
                team_with_ball = ball_change_team(team_with_ball, teams)

        time.sleep(0.15)

    print("Final score ", teams[0]["name"], " ", teams[0]
          ["score"], " : ", teams[1]["name"], " ", teams[1]["score"])


def fut_simulator():

    # Intro art display
    display.intro_art()
    # get names and generate stats
    teams = team_stats.team_generator()
    print(teams[0]["name"], " VS ", teams[1]["name"])
# start the game
    team_with_ball = starts_with_ball(teams)
    print(team_with_ball["name"], "Starts with the ball")

    minute_by_minute(teams, team_with_ball)


fut_simulator()
