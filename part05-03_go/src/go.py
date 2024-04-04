# Write your solution here
def who_won(game_board: list) -> int:
    player1_count = 0
    player2_count = 0
    
    for i in game_board:
        for j in i:
            if j == 1:
                player1_count += 1
            elif j == 2:
                player2_count += 1
    
    if player1_count > player2_count:
        return(1)
    elif player2_count > player1_count:
        return(2)
    else:
        return(0)
