from task2 import list_of_integers_process
import unittest

class TestProcessList(unittest.TestCase):
    def test_valid_input(self):
        input_list = [23,34,56,78,98,90,1,2,3,45]
        output = list_of_integers_process(input_list)
        self.assertEqual(output,[23,98,1])

    def test_invalid_list_size(self):
        input_list = [17,45,34,23,3]
        with self.assertRaises(ValueError):
            output = list_of_integers_process(input_list)

    def test_empty_list(self):
        input_list = []
        output = list_of_integers_process(input_list)
        self.assertEqual(output, [])

    def test_must_integers(self):
        input_list = [0.9,"oops"]
        with self.assertRaises(ValueError):
            output = list_of_integers_process(input_list)

if __name__ == '__main__':
    unittest.main()