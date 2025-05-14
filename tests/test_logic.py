import unittest
import pygame
from game.logic import check_collision

class TestGameLogic(unittest.TestCase):
    def test_collision(self):
        ball = pygame.Rect(100, 100, 20, 20)
        target = pygame.Rect(105, 105, 40, 40)
        self.assertTrue(check_collision(ball, target))

    def test_no_collision(self):
        ball = pygame.Rect(0, 0, 20, 20)
        target = pygame.Rect(300, 300, 40, 40)
        self.assertFalse(check_collision(ball, target))

if __name__ == "__main__":
    unittest.main()
