import unittest


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.a = 3

    def test_dijkstra(self):
        self.assertEqual(self.a, 3)
        

if __name__ == "__main__":
    unittest.main()
