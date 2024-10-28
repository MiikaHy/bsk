import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_game_created(self):
        game = BowlingGame()
        frame = Frame(1,5)
        game.add_frame(frame)
        self.assertEqual(frame, game.get_frame_at(0))
