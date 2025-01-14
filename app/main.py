


def add(numbers: str) -> int:
    if numbers == "":
        return 0
    return sum(int(item) for item in numbers.split(','))
