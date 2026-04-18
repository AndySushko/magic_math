from operator import gt, ge, lt, le, eq, ne


class RomanNum:
    MIN_NUM, MAX_NUM = 1, 3999
    VALUES, ROMANS = [*range(MIN_NUM, MAX_NUM + 1)], []
    for n in range(MIN_NUM, MAX_NUM + 1):
        result = ''
        for value, roman in zip([1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
                                'M CM D CD C XC L XL X IX V IV I'.split()):
            result += n // value * roman
            n %= value
        ROMANS.append(result)
    VAL_ROMAN_DICT = dict(zip(VALUES, ROMANS))
    ROMAN_VAL_DICT = dict(zip(ROMANS, VALUES))

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
        if s not in self.ROMAN_VAL_DICT:
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
        return self.VAL_ROMAN_DICT[num]

    def __to_num(self, stroke: str) -> int:
        return self.ROMAN_VAL_DICT[stroke]


inp = input()
while inp != 'e':
    a = RomanNum(inp)
    b = RomanNum('XXI')
    print(a + b)
    print(type(a))
    inp = input()
