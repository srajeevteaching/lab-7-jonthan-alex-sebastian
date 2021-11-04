# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date:
# Lab Number:
# Program Inputs: Amount of roles the user wants to simulate
# Program Outputs: List containing the sum of each roll, a chart counting the occurrence of a roll

import random


def get_number_of_rolls(input_message):
    number_of_rolls = input(input_message)
    while not number_of_rolls.isdigit():
        number_of_rolls = input(input_message)
    return int(number_of_rolls)


def roll_dice(number):
    simulated_list = []
    for i in range(number):
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        dice_total = dice_one + dice_two
        simulated_list.append(dice_total)
    return simulated_list


def create_histogram_list(list_of_roles):
    counted_list = []
    count = 2
    i = 0
    while i <= 10:
        count_variable = list_of_roles.count(count)
        counted_list.append(count_variable)
        count += 1
        i += 1
    return counted_list


def print_histogram(histogram_list):
    i = 0
    counter = 2
    while i <= 10:
        print(str(counter) + ":\t" + ("*" * histogram_list[i]))
        counter += 1
        i += 1


def main():
    user_number_rolls = get_number_of_rolls("How many times would you like to roll: ")
    list_of_all_rolls = roll_dice(user_number_rolls)
    counted_rolls_list = create_histogram_list(list_of_all_rolls)
    print(counted_rolls_list)
    print_histogram(counted_rolls_list)


main()
