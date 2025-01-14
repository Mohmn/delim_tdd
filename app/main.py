from typing import List


class InvalidDelemiterException(Exception):
    pass


class NegativeNumberException(Exception):
    def __init__(self, negatives: List[str]):
        self.negatives = negatives
        super().__init__(f"Negatives not allowed: {', '.join(map(str, negatives))}")



def isDigit(char: str) -> bool:
    try:
        int(char)
        return True
    except ValueError:
        return False

class DelimeterParser:
    def __init__(self, numbers: str):
        self.numbers = numbers
        self.delimiters = set()
        self.parse_numbers_from = 0
        self._parse_delims()

    def _parse_delims(self):
        if self.numbers[0:2] == "//":
            self.custom_delims_present = True
            i = 2
            delim = ""
            char = ""
            while char != "\n":
                char = self.numbers[i]
                if char == "[":
                    delim = ""
                elif char == "]":
                    self.delimiters.add(delim)
                    delim = ""
                else:
                    delim += char
                i += 1
            self.parse_numbers_from = i
        else:
            self.delimiters.add("\n")
            self.delimiters.add(",")

    def parse(self):
        number = ""
        num_len = len(self.numbers)
        delim = ""
        i = self.parse_numbers_from
        while i < num_len:
            char = self.numbers[i]
            if number == "" and char == "-":
                number += char
                i += 1
                continue
            if isDigit(char):
                if delim:
                    if delim not in self.delimiters:
                        raise InvalidDelemiterException("Invalid Delimeter")
                    delim = ""
                number += char
            else:
                if number:
                    yield number
                    number = ""
                delim += char
            i += 1

        if number:
            if number == "-":
                raise InvalidDelemiterException("Invalid Delimeter")
            yield number

    def sum(self):
        neg_numbers = []
        summation = 0
        for num in self.parse():
            if float(num) < 0:
                neg_numbers.append(num)
            if float(num) < 1001:
                summation += float(num)
        if len(neg_numbers) > 0:
            raise NegativeNumberException(neg_numbers)
        return summation

def add(numbers: str) -> int:
    delimeterParser = DelimeterParser(numbers)
    return delimeterParser.sum()
