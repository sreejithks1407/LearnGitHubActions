import random


def choose_midfielder(available_midfielders, total_mifielders_needed):

    available_midfielders_number = len(available_midfielders)
    selected_numbers = []

    # total_mifielders_needed = int(input(
    #     "Provide the number of midfielders needed in your squad for today's match \n"))

    while (total_mifielders_needed > available_midfielders_number):
        total_mifielders_needed = int(input(
            f'Total midfielders available for selection is {available_midfielders_number} which less than your requirement. So please select a number which is less than or equal to this.'))

    total_midfielders_choosen = 0

    while total_midfielders_choosen < total_mifielders_needed:

        random_palyer_number = random.randint(0, 4)
        if random_palyer_number not in selected_numbers:
            selected_numbers.append(random_palyer_number)
            total_midfielders_choosen += 1

    my_midfielder_combinations_for_todays_game = [
        available_midfielders[player_number] for player_number in selected_numbers]

    return my_midfielder_combinations_for_todays_game


# midfielders_for_match_day = choose_midfielder(available_midfielders_list)
# print(midfielders_for_match_day)
