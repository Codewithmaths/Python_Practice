import unittest
from a import canVisitAllRooms

class TestCanVisitAllRooms(unittest.TestCase):

    def test_example_1(self):
        self.assertTrue(canVisitAllRooms([[1],[2],[3],[]]))

    def test_example_2(self):
        self.assertFalse(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

    def test_all_rooms_locked(self):
        self.assertFalse(canVisitAllRooms([[],[1],[2],[3]]))

    def test_single_room(self):
        self.assertTrue(canVisitAllRooms([[]]))

    def test_circular_dependency(self):
        self.assertTrue(canVisitAllRooms([[1],[2],[0]]))

if __name__ == '__main__':
    unittest.main()
