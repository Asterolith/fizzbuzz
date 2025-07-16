#_class FizzbuzzLogic: encapsulted and modifiable with custom rules
from typing import Dict, List, Optional

# default global rules
DEFAULT_RULES: Dict[int, str] = {3: "Fizz", 5: "Buzz"}


def validate_range(start: int, end: int) -> None:
    if start < 1 or end < 1 or start > end:
        raise ValueError(f"Invalid range: start={start}, end={end}")


def validate_rules(rules: Dict[int, str]) -> None:
    if any(divisor == 0 for divisor in rules):
        raise ZeroDivisionError("Divisor cannot be zero in rules")


class FizzBuzzLogic:
    """
    Encapsulates FizzBuzz logic with custom rules and range.

    Usage example:
        fb = FizzBuzzLogic(start=1, end=100, rules={3: "Fizz", 5: "Buzz"})
        output = fb.run()
    """
    def __init__(self, 
                 start: int = 1, 
                 end: int = 100, 
                 rules: Optional[Dict[int, str]] = None
                 ) -> None:
        validate_range(start, end)
        self.start = start
        self.end = end

        #_avoid mutation of default rules
        self.rules = rules.copy() if rules is not None else DEFAULT_RULES.copy()
        validate_rules(self.rules)


    def fizzbuzz_logic_adv(self, num: int, 
                           rules: Optional[Dict[int, str]] = None) -> str:
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
        fb_rules = rules.copy() if rules is not None else self.rules

        #_check zero/divisor conflict
        if num == 0 and any(divisor == 0 for divisor in fb_rules):
            raise ZeroDivisionError("Cannot process num=0 with zero divisor in rules")

        #_check for exact match (except num=0)
        if num in fb_rules and num != 0:
            return fb_rules[num]

        output: List[str] = []
        for divisor, word in fb_rules.items():
            if divisor == 0:
                continue

            if num % divisor == 0:
                output.append(word)

        return "".join(output) or str(num)
    

    def run(self, rules: Optional[Dict[int, str]] = None) -> List[str]:
        """
        Runs the FizzBuzz logic for a range of numbers with customizable rules.
        """
        fb_rules = rules.copy() if rules is not None else self.rules
        validate_rules(fb_rules)

        self.result = [
            self.fizzbuzz_logic_adv(i)
            for i in range(self.start, self.end + 1)
        ]
        return self.result
    

    def fizzbuzz_logic(self, num: int) -> str:
        """
        Basic FizzBuzz: hard‑coded for 3, 5, and both.
        """
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:

            return str(num)


if __name__ == "__main__":
    # Default 1–100, Fizz/Buzz default rules
    fb = FizzBuzzLogic()
    for line in fb.run():
        print(line)