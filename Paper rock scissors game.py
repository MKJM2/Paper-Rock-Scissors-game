choice =''
while choice != 'n':
    
    choice = input('Do you want to play the game? ').lower()

    while choice == 'y':
        p_1 = input("What is Player 1's request?\n\n").lower()
        p_2 = input("What is Player 2's reguest?\n\n").lower()

        choices = ['paper', 'rock', 'scissors']

        if p_1 not in choices:
            print('You a goof.')
        if p_2 not in choices:
            print('You a goof.')



        if p_1 and p_2 in choices:

                if p_1 == p_2:
                    print("It's a draw!")

                if choices.index(p_1) == (choices.index(p_2) + 1) % 3:
                    print('Player 2 Wins!')

                if choices.index(p_2) == (choices.index(p_1) + 1) % 3:
                    print('Player 1 Wins!')

        break
quit()



    
    
