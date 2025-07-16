#_unit test for fizzbuzz() and fizzbuzz_logic_adv()
import unittest
from fizzbuzz import fizzbuzz
from FizzbuzzLogic import FizzBuzzLogic

RULES = {3: "Fizz", 5: "Buzz"}
fb = FizzBuzzLogic()

class TestFizzBuzz(unittest.TestCase):

    def test_solo_value(self):
        self.assertEqual(fb.fizzbuzz_logic(1), "1")
        self.assertEqual(fb.fizzbuzz_logic(3), "Fizz")
        self.assertEqual(fb.fizzbuzz_logic(5), "Buzz")
        self.assertEqual(fb.fizzbuzz_logic(15), "FizzBuzz")

        self.assertEqual(fb.fizzbuzz_logic_adv(7, RULES), "7")
        self.assertEqual(fb.fizzbuzz_logic_adv(100, RULES), "Buzz")
        self.assertEqual(fb.fizzbuzz_logic_adv(3, RULES), "Fizz")
        self.assertEqual(fb.fizzbuzz_logic_adv(15, RULES), "FizzBuzz")


    def test_range_values(self):
        result = fizzbuzz(1, 15)
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", 
                    "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
        self.assertEqual(result, expected)


    def test_multiples(self):
        for i in range(1, 101):
            value = fb.fizzbuzz_logic_adv(i, RULES)
            if i % 3 == 0 and i % 5 == 0:
                self.assertEqual(value, "FizzBuzz")
            elif i % 3 == 0:
                self.assertEqual(value, "Fizz")
            elif i % 5 == 0:
                self.assertEqual(value, "Buzz")
            else:
                self.assertEqual(value, str(i))

    
    def test_zero_and_negative(self):
        #_Zero should return FizzBuzz, 0 modulo any divisor
        self.assertEqual(fb.fizzbuzz_logic(0), "FizzBuzz")
        self.assertEqual(fb.fizzbuzz_logic_adv(0, RULES), "FizzBuzz")

        #_Negative multiples not defined in requirements
        cases = [
            (-3,  "Fizz"),
            (-5,  "Buzz"),
            (-15, "FizzBuzz"),
            (-8,  "-8") 
        ]
        for num, expected in cases:
            self.assertEqual(fb.fizzbuzz_logic(num), expected)
            self.assertEqual(fb.fizzbuzz_logic_adv(num, RULES), expected)


    def test_custom_rules(self):
        #_overlapping rules
        rules1 = {2: "Foo", 4: "Bar"}
        self.assertEqual(fb.fizzbuzz_logic_adv(2, rules1), "Foo")
        self.assertEqual(fb.fizzbuzz_logic_adv(4, rules1), "Bar")
        self.assertEqual(fb.fizzbuzz_logic_adv(12, rules1), "FooBar")  

        #_zero divisor
        rules2 = {2: "Foo", 3: "Bar", 0: "Zero"}
        with self.assertRaises(ZeroDivisionError):
            fb.fizzbuzz_logic_adv(0, rules2)

        self.assertEqual(fb.fizzbuzz_logic_adv(2, rules2), "Foo")
        self.assertEqual(fb.fizzbuzz_logic_adv(3, rules2), "Bar")
        self.assertEqual(fb.fizzbuzz_logic_adv(6, rules2), "FooBar")
    

def main():
    unittest.main()