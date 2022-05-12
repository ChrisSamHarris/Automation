import random

full_list = ['Tom', 'Lee', 'Ant', 'Ste', 'DaveH', 'Yousef', 'Ralphy', 'Max', 'Rusty1', 'Rusty2']

white_team = []
black_team = []

while len(full_list) >= 1:
    for name in full_list:
        first_name = random.choice(full_list)
        full_list.remove(first_name)
        if len(white_team) < 5:
            white_team.append(first_name)
        else:
            black_team.append(first_name)

print(f"White Colours:{white_team}")
print(f"Black Colours:{black_team}")


##### Based on self-evaluated ratings we can also select skill-matched teams #####

complete_players = {'Tom':6, 'Lee': 8, 'Ant': 6, 'Ste': 5, 'DaveH': 5, 'Yousef': 9, 'Ralphy': 3, 'Max': 6, 'Rusty1': 5, 'Rusty2': 5}

good_team = []
bad_team = []

for person, rating in complete_players.items():
    good_total_rating = 0
    bad_total_rating = 0
    if rating >= 6:
        good_team.append(person)
        good_total_rating += rating
    elif rating < 6:
        bad_team.append(person)
        bad_total_rating += rating
