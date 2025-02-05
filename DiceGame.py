import random

def check_winner(player_steps, opponent_steps):
    """Check if a player has won and stop the game."""
    if player_steps >= 20:
        print("\n🎉 Congratulations! You reached 20 steps first. You win!")
        return True
    if opponent_steps >= 20:
        print("\n💀 Oh no! The opponent reached 20 steps first. You lose!")
        return True
    return False

def opponent_turn(steps):
    """Handles the opponent's turn."""
    print("\nOpponent's turn...")
    while True:
        dice_roll = random.randint(1, 6)
        print(f"Opponent rolled a {dice_roll}")
        steps += dice_roll
        
        if check_winner(player_steps, steps):  # Check if opponent won
            return steps, True  # End game
        
        if dice_roll != 6:
            break
        print("Opponent got a 6! Rolling again...")

    return steps, False  # Continue game

def player_turn(steps):
    """Handles the player's turn."""
    print("\nYour turn...")
    while True:
        input("Press Enter to roll the dice...")  # Wait for player input
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll}")
        steps += dice_roll
        
        if check_winner(steps, opponent_steps):  # Check if player won
            return steps, True  # End game
        
        if dice_roll != 6:
            break
        print("You got a 6! Rolling again...")

    return steps, False  # Continue game

# --- Main Code ---
player_steps, opponent_steps = 0, 0

# Deciding who starts first
turn = "player" if random.randint(1, 2) == 2 else "opponent"
print(f"\n{turn.capitalize()} goes first!")

# Turn switching dictionary
turns = {"player": "opponent", "opponent": "player"}

game_over = False  # Game control flag

while not game_over:
    if turn == "player":
        player_steps, game_over = player_turn(player_steps)
    else:
        opponent_steps, game_over = opponent_turn(opponent_steps)
    
    if not game_over:  # Switch turns only if game is still on
        turn = turns[turn]
