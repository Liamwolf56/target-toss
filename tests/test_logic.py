import unittest
import pygame
from game.logic import check_collision

class TestLogic(unittest.TestCase):
    def test_collision(self):
        ball = pygame.Rect(50, 50, 10, 10)
        target = pygame.Rect(55, 55, 20, 20)
        self.assertTrue(check_collision(ball, target))

    def test_no_collision(self):
        ball = pygame.Rect(0, 0, 10, 10)
        target = pygame.Rect(100, 100, 20, 20)
        self.assertFalse(check_collision(ball, target))

if __name__ == "__main__":
    unittest.main()

