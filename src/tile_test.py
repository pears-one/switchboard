import unittest
from tile import Tile

class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = Tile(1,2,2,0,0)

    def test_top_is_playable(self):
       self.assertTrue(self.tile.top_is_playable(0))
       self.assertTrue(self.tile.top_is_playable(1))
       self.assertFalse(self.tile.top_is_playable(2))
       self.assertFalse(self.tile.top_is_playable(3))
       self.assertTrue(self.tile.top_is_playable(204))

    def test_left_is_playable(self):
       self.assertTrue(self.tile.left_is_playable(0))

    def test_right_is_playable(self):
       self.assertFalse(self.tile.right_is_playable(0))

    def test_bottom_is_playable(self):
       self.assertFalse(self.tile.bottom_is_playable(0))

if __name__ == '__main__':
    unittest.main()