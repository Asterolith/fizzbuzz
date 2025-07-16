#_fizzbuzz.py
from typing import Dict, List, Optional
from FizzbuzzLogic import FizzBuzzLogic

#_Custom rules for fizzbuzz
RULES = {3: "Fizz", 5: "Buzz"}


def fizzbuzz(start: int, end: int, 
             rules: Optional[Dict[int, str]] = None) -> List[str]:
    """
    Returns the FizzBuzz results for a range of numbers with customizable rules.
    """
    fb = FizzBuzzLogic(start, end, rules = RULES.copy())
    return fb.run()


if __name__ == "__main__":
    #_Default 1–100, Fizz/Buzz rules
    results = fizzbuzz(1, 100)
    for line in results:
        print(line)

#--------------------------------------------
#_Logic before encapsulation
def fizzbuzz_logic_adv(num, rules):
    """
    Returns a string, either a number, or a FizzBuzz result based on customizable rules.

    Args:
        num (int): The number to evaluate.
        rules (dict): A dictionary where the keys are the divisors and the values are the corresponding words.

    Returns:
        str: The FizzBuzz result for the given number based on the customizable rules.

    Raises:
        ZeroDivisionError: If a divisor of zero is given in the rules.
    """
    #_First check for exact match between number and rule (catch divisor of zero)
    if num in rules:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return rules[num]


    #_Check for multiple matches and concatenate words
    output = ""
    for divisor, word in rules.items():
        if divisor == 0:
            continue

        if num % divisor == 0:
            output += word

    return output or str(num)