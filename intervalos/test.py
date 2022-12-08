import unittest
from main import intervals

class TestCase(unittest.TestCase):
    
    def test_no_elements(self):
        result = intervals([])
        self.assertEqual(result, "[]")
    
    def test_one_element(self):
        result = intervals([3])
        self.assertEqual(result, "[3]")

    def test_simple_list(self):
        result = intervals([100, 101])
        self.assertEqual(result, "[100-101]")

    def test_three_numbers(self):
        result = intervals([1, 2, 3])
        self.assertEqual(result, "[1-3]")

    def test_two_sequence(self):
        result = intervals([1,2,3,5,6])
        self.assertEqual(result, "[1-3], [5-6]")
        
    def test_many_sequences(self):
        result = intervals([100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150])
        self.assertEqual(result, "[100-105], [110-111], [113-115], [150]")


if __name__ == "__main__":
    unittest.main()