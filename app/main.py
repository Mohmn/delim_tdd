class InvalidDelemiterException(Exception):
    pass


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
            if char.isdigit():
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
            yield number

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimeterParser = DelimeterParser(numbers)
    return sum(int(item) for item in delimeterParser.parse())
