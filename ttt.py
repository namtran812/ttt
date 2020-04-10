
# Defines game


def play_game():

    #introduction and rules
    print('\nWelcome to Tic Tac Toe! \n')
    print('Rules of the game: Input the number where you')
    print('would like to place your move corresponding to')
    print('the chart below. First to line up 3 symbols wins! \n')
    print('1' + '|' + '2' + '|' + '3')
    print('-----')
    print('4' + '|' + '5' + '|' + '6')
    print('-----')
    print('7' + '|' + '8' + '|' + '9')


# Player assignment
    player1 = input('\nPlayer 1: Do you want to be X or O? ')

    if player1.lower() == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    # Game start prompt
    print('Player 1 will go first')
    play = input('Are you ready to play? Enter Yes or No. ')

    # Game play

    if play.lower() == 'yes':

        result = True
        boardlist = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        onewin = ['player1', 'player1', 'player1']
        twowin = ['player2', 'player2', 'player2']

        def board():
            print(boardlist[1] + '|' + boardlist[2] + '|' + boardlist[3])
            print('-----')
            print(boardlist[4] + '|' + boardlist[5] + '|' + boardlist[6])
            print('-----')
            print(boardlist[7] + '|' + boardlist[8] + '|' + boardlist[9])

        x = 0

        while result == True:

            board()
            player_one_move = input("Player 1's move: ")
            boardlist[int(player_one_move)] = player1
            print('\n'*100)
            board()
            if boardlist[1] == boardlist[2] == boardlist[3] == player1:
                print('Player 1 wins!')
                break

            if boardlist[4] == boardlist[5] == boardlist[6] == player1:
                print('Player 1 wins!')
                break

            if boardlist[7] == boardlist[8] == boardlist[9] == player1:
                print('Player 1 wins!')
                break

            if boardlist[1] == boardlist[4] == boardlist[7] == player1:
                print('Player 1 wins!')
                break

            if boardlist[2] == boardlist[5] == boardlist[8] == player1:
                print('Player 1 wins!')
                break

            if boardlist[3] == boardlist[6] == boardlist[9] == player1:
                print('Player 1 wins!')
                break

            if boardlist[1] == boardlist[5] == boardlist[9] == player1:
                print('Player 1 wins!')
                break

            if boardlist[3] == boardlist[5] == boardlist[9] == player1:
                print('Player 1 wins!')
                break

            x += 1

            if x == 5:
                print("\nIt's a draw!")
                break

            player_two_move = input("Player 2's move: ")
            boardlist[int(player_two_move)] = player2
            print('\n'*100)
            if boardlist[1] == boardlist[2] == boardlist[3] == player2:
                print('\n'*100)
                print('Player 2 wins!')
                board()
                break

            if boardlist[4] == boardlist[5] == boardlist[6] == player2:
                print('\n'*100)
                print('Player 2 wins!')
                board()
                break

            if boardlist[7] == boardlist[8] == boardlist[9] == player2:
                print('\n'*100)
                print('Player 2 wins!')
                board()
                break

            if boardlist[1] == boardlist[4] == boardlist[7] == player2:
                print('\n'*100)
                print('Player 2 wins!')
                board()
                break

            if boardlist[2] == boardlist[5] == boardlist[8] == player2:
                print('\n'*100)
                print('Player 2 wins!')
                board()
                break

            if boardlist[3] == boardlist[6] == boardlist[9] == player2:
                print('\n'*100)
                print('Player 2 wins!')
                board()
                break

            if boardlist[1] == boardlist[5] == boardlist[9] == player2:
                print('\n'*100)
                print('Player 2 wins!')
                board()
                break

            if boardlist[3] == boardlist[5] == boardlist[7] == player2:
                print('\n'*100)
                print('Player 2 wins!')
                board()
                break


# Game loop
play_call = True

while play_call == True:
    play_game()
    play_again = input('\nWould you like to play again? ')
    if play_again.lower() == 'yes':
        continue
    else:
        print('Thanks for playing!')
        play_call = False
