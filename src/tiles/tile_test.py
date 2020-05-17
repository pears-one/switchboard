import unittest
from tiles import Tile, RotatedTile
from tiles.spots import LeftSpot, RightSpot, MiddleSpot
from config.constants import LEFT, RIGHT, BELOW, ABOVE


class TestTile(unittest.TestCase):
    def setUp(self):
        spots = [LeftSpot(1), RightSpot(1), MiddleSpot(1)]
        self.tile = Tile(spots)

    def test_is_accessible_from(self):
        self.assertTrue(self.tile.is_accessible_from(LEFT))
        self.assertTrue(self.tile.is_accessible_from(RIGHT))
        self.assertFalse(self.tile.is_accessible_from(ABOVE))
        self.assertFalse(self.tile.is_accessible_from(BELOW))


class TestRotatedTile(unittest.TestCase):
    def setUp(self):
        spots = [LeftSpot(1), RightSpot(1), MiddleSpot(1)]
        self.one_rotation_tile = RotatedTile(spots, 1)

    def test_is_accessible_from(self):
        self.assertFalse(self.one_rotation_tile.is_accessible_from(LEFT))
        self.assertFalse(self.one_rotation_tile.is_accessible_from(RIGHT))


if __name__ == '__main__':
    unittest.main()
