from smallest_number_calculator import smallest
import unittest

class Test_Smallest_Number_Calculator(unittest.TestCase):

    def test_input_type(self):
        with self.assertRaises(TypeError) as context:
            smallest('string')
        self.assertTrue('Input must be an integer value',context.exception)

    def test_inputs(self): 
        self.assertEqual(smallest(261235), [126235, 2, 0])
        self.assertEqual(smallest(209917), [29917, 0, 1])
        self.assertEqual(smallest(285365), [238565, 3, 1])
        self.assertEqual(smallest(269045), [26945, 3, 0])
        self.assertEqual(smallest(296837), [239687, 4, 1])

unittest.main()