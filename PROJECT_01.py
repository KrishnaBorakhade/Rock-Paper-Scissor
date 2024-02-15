import random

count_user = 0
count_com = 0

while True:
    user_input = input("Enter your choice \n 0. ROCK \n 1. PAPER \n 2. SCISSOR or 'q' to quit: ")
    
    if user_input.lower() == 'q':
        break
    
    if user_input not in ['0', '1', '2']:
        print("Invalid input. Please enter '0', '1', '2', or 'q' to quit.")
        continue
    
    user = int(user_input)
    com = random.randint(0,2)
    
    if user == com:
        print('Match drawn ...')
    elif (user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1):
        print('Hurray! You have won ...')
        count_user += 1
    else:
        print('You have lost...')
        count_com += 1

print("Game Over")

if count_com > count_user:
    print("Your score:", count_user)
    print("You have lost the game by", count_com - count_user, "points")
elif count_user > count_com:
    print("Your score:", count_user)
    print("Hurray! You have won the game by", count_user - count_com, "points")
else:
    print("The game is drawn...")
    print("Your score:", count_user)
