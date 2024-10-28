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

    def test_empty_game(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at, 0)

    def test_game_created_with_10_frames(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))

        frame = Frame(2, 6)
        game.add_frame(frame)

        self.assertEqual(frame, game.get_frame_at(9))

    def test_game_created_with_11_frames(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))

        frame = Frame(2, 6)
        game.add_frame(frame)

        self.assertRaises(BowlingError, game.add_frame, Frame(1,1))

    def test_calculate_score(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))

        frame = Frame(2, 6)
        game.add_frame(frame)

        self.assertEqual(81, game.calculate_score())

    def test_calculate_score_with_spare(self):
        game = BowlingGame()

        game.add_frame(Frame(9, 1))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))

        frame = Frame(2, 6)
        game.add_frame(frame)

        self.assertEqual(88, game.calculate_score())

    def test_calculate_score_with_strike(self):
        game = BowlingGame()

        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))

        frame = Frame(2, 6)
        game.add_frame(frame)

        self.assertEqual(94, game.calculate_score())

    def test_calculate_score_with_strike_and_spare(self):
        game = BowlingGame()

        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(4, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))

        frame = Frame(2, 6)
        game.add_frame(frame)

        self.assertEqual(103, game.calculate_score())

    def test_calculate_score_with_strike_following_strike(self):
        game = BowlingGame()

        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))

        frame = Frame(2, 6)
        game.add_frame(frame)

        self.assertEqual(112, game.calculate_score())