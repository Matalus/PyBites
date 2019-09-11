games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def print_game_stats(games_won=games_won):
    for person, games in games_won.items():
        plural = "" if games == 1 else "s"
        print(f"{person} has won {games} game{plural}")

print_game_stats()