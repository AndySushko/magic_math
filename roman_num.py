from operator import gt, ge, lt, le, eq, ne


class RomanNum:
    MIN_NUM, MAX_NUM = 1, 3999
    ROMAN_DICT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    VALUES = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    ROMANS = 'M CM D CD C XC L XL X IX V IV I'.split()
    ROMAN_SET = set()
    for n in range(1, 4000):
        result = ''
        for value, roman in zip(VALUES, ROMANS):
            result += n // value * roman
            n %= value
        ROMAN_SET.add(result)

    def __init__(self, data):
        if isinstance(data, int):
            if not (self.MIN_NUM <= data <= self.MAX_NUM):
                raise ValueError(f'the RomanNum value must be between {self.MIN_NUM} and {self.MAX_NUM}: {data}')
        elif isinstance(data, str):
            stroke = data.replace(' ', '')
            self.__is_roman(stroke)
            data = self.__to_num(stroke)
        else:
            raise TypeError(f'the RomanNum object can only accept int or str, not: {data, type(data)}')
        self.value = data
        self.roman = self.__to_roman(data)

    def __repr__(self):
        return f'RomanNum({self.value})'

    def __str__(self):
        return self.roman

    def __int__(self):
        return self.value

    def __index__(self):
        return self.value

    def __eq__(self, other):
        return self.__compare(other, '==')

    def __gt__(self, other):
        return self.__compare(other, '>')

    def __ge__(self, other):
        return self.__compare(other, '>=')

    def __lt__(self, other):
        return self.__compare(other, '<')

    def __le__(self, other):
        return self.__compare(other, '<=')

    def __ne__(self, other):
        return self.__compare(other, '!=')

    def __add__(self, other):
        if isinstance(other, int):
            return RomanNum(self.value + other)
        elif isinstance(other, str):
            self.__is_roman(other)
            return RomanNum(self.value + self.__to_num(other))
        elif type(other) == type(self):
            return RomanNum(self.value + other.value)
        else:
            raise TypeError("A RomanNum object can be added to int, str, RomanNum object.")

    def __is_roman(self, s: str):
        if s not in self.ROMAN_SET:
            raise ValueError(f'the string param in RomanNum is not correct roman numeral: "{s}"')

    def __compare(self, other, comparison_sign):
        ops = {'>': gt, '>=': ge, '<': lt, '<=': le, '==': eq, '!=': ne}
        if isinstance(other, int):
            return ops[comparison_sign](self.value, other)
        elif isinstance(other, str):
            self.__is_roman(other)
            return ops[comparison_sign](self.value, self.__to_num(other))
        elif type(other) == type(self):
            return ops[comparison_sign](self.value, other.value)
        else:
            raise TypeError("A RomanNum object can be tested for equality with int, str, RomanNum.")

    def __to_roman(self, num: int) -> str:
        result = ''
        for value, roman in zip(self.VALUES, self.ROMANS):
            result += num // value * roman
            num %= value
        return result

    def __to_num(self, stroke: str) -> int:
        nums = [self.ROMAN_DICT[char] for char in stroke] + [0]
        return sum(-nums[i] if nums[i + 1] > nums[i] else nums[i] for i in range(len(nums) - 1))


inp = input()
while inp != 'e':
    a = RomanNum(inp)
    b = RomanNum('XXI')
    print(a + b)
    print(type(a))
    inp = input()
