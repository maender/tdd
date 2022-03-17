import unittest
from unittest.mock import Mock, patch
from modules.bowling import bowling_score
from modules.game import Game

GAME1 = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
GAME2 = [10, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def create_empty_game():
    return [0 for x in range(20)]

class Display:
    def __init__(self) -> None:
        pass

    def display_score(self, score):
        print(score)

class PinCollector:
    def __init__(self) -> None:
        pass

    def fallen(self):
        pass

class TestBowling(unittest.TestCase):
    def test_empty(self):
        d = Display()
        pc = PinCollector()
        pc.fallen = Mock(side_effect=GAME1) #STUB
        d.display_score = Mock()
        g = Game(pc, d)
        g.play()
        d.display_score.assert_called_once_with(3)

    def test_strike(self):
        d = Display()
        pc = PinCollector()
        pc.fallen = Mock(side_effect=GAME2)
        d.display_score = Mock()
        Game(pc, d).play()
        d.display_score.assert_called_once_with(28)


if __name__ == '__main__':
    unittest.main()