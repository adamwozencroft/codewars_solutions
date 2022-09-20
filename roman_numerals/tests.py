from roman_numerals_encoder import solution
import unittest

class Test_Roman_Numerals_Encoder(unittest.TestCase):

    def test_input_type(self):
        with self.assertRaises(TypeError) as context:
            solution('string')
        self.assertTrue('Error: Input year must be an integer.' in str(context.exception))

    def test_inputs(self):
        self.assertEqual(solution(1),'I', "solution(1),'I'")
        self.assertEqual(solution(4),'IV', "solution(4),'IV'")
        self.assertEqual(solution(6),'VI', "solution(6),'VI'")
        self.assertEqual(solution(14),'XIV', "solution(14),'XIV")
        self.assertEqual(solution(21),'XXI', "solution(21),'XXI'")
        self.assertEqual(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
        self.assertEqual(solution(91),'XCI', "solution(91),'XCI'")
        self.assertEqual(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
        self.assertEqual(solution(1000), 'M', 'solution(1000), M')
        self.assertEqual(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
        self.assertEqual(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")

unittest.main()