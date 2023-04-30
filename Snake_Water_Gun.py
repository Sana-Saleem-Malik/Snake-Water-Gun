import random
point_of_computer = 0
point_of_user = 0

choices = {'S': 0, 'W': 1, 'G': 2}
cases = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]


def play_round(player_turn):
    global point_of_computer
    global point_of_user
    computer_turn = random.randint(0, 2)
    player_index = choices[player_turn]
    result = cases[player_index][computer_turn]

    if result == 0:
        print("\n")
        print("Tie!")
        print("\n")
    elif result == 1:
        print("\n")
        print("You Win!")
        print("\n")
        point_of_user += 1
        print(f"Your Points: {point_of_user}")
        print("\n")
    else:
        print("Computer Win!")
        print("\n")
        point_of_computer += 1
        print(f"Computer Points: {point_of_computer}")
        print("\n")


while True:
    print("\n")
    try:
        player_turn = input(
            "Enter S for Snake, W for Water, G for Gun, or Q to quit: Q ")
        print("\n")

        if player_turn.upper() == "Q":
            print(
                f"you win: {point_of_user} times\ncomputer win: {point_of_computer} times")
            break
        play_round(player_turn.upper())
    except:
        print("Invalid input. Please enter S, W, G, or Q.")
