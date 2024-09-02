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
