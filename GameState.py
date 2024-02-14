



players = []

global current_turn
current_turn = "White"

def next_turn():
    global current_turn
    if current_turn == "White":
        current_turn = "Black"
    else:
        current_turn = "White"
        