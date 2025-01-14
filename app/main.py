
class DelimeterParser:
    def __init__(self, numbers: str):
        self.numbers = numbers
        self.delimiters = set(["\n", ","])

    def parse(self):
        number = ""
        num_len = len(self.numbers)
        delim = ""
        i = 0
        while i < num_len:
            char = self.numbers[i]
            if char.isdigit():
                if delim:
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
