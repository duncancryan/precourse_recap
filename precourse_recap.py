# I'm establishing my global variables here to be used in conditionals later

fav_game = "The Witcher 3"
second_fav_game = "The Outer Wilds"
fav_film = "Lord of the Rings: The Return of the King"
second_fav_film = "City of God"

# This is my first user input which sets up the 'parent' conditional

game_answer = input("Do you enjoy playing video games? (Yes/No) ")
if game_answer == "Yes":
    user_game = input("Nice! What is your favourite game? ")
    if user_game == fav_game or user_game == second_fav_game:
        print("No way! I love that game!")
    else:
        print("I have heard that game is great! I need to play it")
else:
    user_film = input("Fair Enough! Well what is your favourite film? ")
    if user_film == fav_film or user_film == second_fav_film:
        print("You've got brilliant taste!")
    else:
        print("I'll make sure to watch it!")
print("Goodbye!")