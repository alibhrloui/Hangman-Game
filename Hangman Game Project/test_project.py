from unittest.mock import patch
import builtins
import project

def test_ready_player():
    with patch.object(builtins, 'input', side_effect=['$&*','1425125','mj','david']):
        project.ready_player()
        return

def test_gaming():
    global miss
    miss = 0
    guesses = iter(['A', 'B', 'C', 'D', 'E'])
    with patch.object(builtins, 'input', side_effect=lambda _: next(guesses)):
        project.gaming()

def test_game_over():
    global miss, hearts
    miss = 0  # Set the value of "miss" to simulate a win
    hearts = 6  # Set the value of "hearts" to simulate a win

    with patch('builtins.input', return_value=''):
        project.game_over()

