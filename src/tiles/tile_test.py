import unittest
from tiles.tiles import Tile, RotatedTile
from tiles.tile_id import TileID
from spots.spots import Spot
from spots.spot_positions import SpotPositionFactory
from config.constants import LEFT, RIGHT, BELOW, ABOVE, LEFT_SPOT, MIDDLE_SPOT, RIGHT_SPOT


class TestTile(unittest.TestCase):
    def setUp(self):
        fac = SpotPositionFactory()
        spots = [Spot(fac.get_by_id(LEFT_SPOT), 1), Spot(fac.get_by_id(MIDDLE_SPOT), 1), Spot(fac.get_by_id(RIGHT_SPOT), 1)]
        self.tile = Tile(TileID(1, 1), spots)

    def test_is_accessible_from(self):
        self.assertTrue(self.tile.is_accessible_from(LEFT))
        self.assertTrue(self.tile.is_accessible_from(RIGHT))
        self.assertFalse(self.tile.is_accessible_from(ABOVE))
        self.assertFalse(self.tile.is_accessible_from(BELOW))


class TestRotatedTile(unittest.TestCase):
    def setUp(self):
        fac = SpotPositionFactory()
        spots = [Spot(fac.get_by_id(LEFT_SPOT), 1), Spot(fac.get_by_id(MIDDLE_SPOT), 1), Spot(fac.get_by_id(RIGHT_SPOT), 1)]
        self.one_rotation_tile = RotatedTile(TileID(1, 1), spots, 1)

    def test_is_accessible_from(self):
        self.assertFalse(self.one_rotation_tile.is_accessible_from(LEFT))
        self.assertFalse(self.one_rotation_tile.is_accessible_from(RIGHT))


if __name__ == '__main__':
    unittest.main()
