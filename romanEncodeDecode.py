'''
Task
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below.
 Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
 '''
 
 class RomanNumerals:
    def __init__(self):
        self.abc = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        self.num = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        self.orNum = [1000, 500, 100, 50, 10, 5, 1]
    def to_roman(self, num):
        n = len(str(num))-1
        parts = []
        rmP = []
        i = 0
        c = 0
        while n > -1:
            parts.append(str(num)[i] + '0' * n)
            n -= 1
            i += 1
        for i in parts[:]:
            if int(i) == 0:
                parts.remove(i)
        for i in parts:
            i = int(i)
            while i >= 2000:
                rmP.append('M')
                i-=1000
            if i in self.num:
                rmP.append(self.num[i])
            else:
                for x in self.num:
                    if i == x - 1:
                        rmP.append('I' + self.num[x])
                        c = 1
                    elif i == x - 5:
                        rmP.append('V' + self.num[x])
                        c = 1
                    elif i == x - 10:
                        rmP.append('X' + self.num[x])
                        c = 1
                    elif i == x - 50:
                        rmP.append('L' + self.num[x])
                        c = 1
                    elif i == x - 100:
                        rmP.append('C' + self.num[x])
                        c = 1
                    elif i == x - 500:
                        rmP.append('D' + self.num[x])
                        c = 1
                    elif i == x - 1000:
                        rmP.append('M' + self.num[x])
                        c = 1
                if c != 1:
                    for x in self.orNum:
                        if i > x:
                            rmP.append(self.num[x])
                            i -= x
                            while i != 0:
                                rmP.append('I')
                                i -= 1
                            c = 0
                            break
        return ''.join(rmP)
    def from_roman(self, inp):
        total = 0
        i = 0
        while i < len(inp):
            if i != len(inp)-1 and self.abc[inp[i+1]] > self.abc[inp[i]]:
                total += self.abc[inp[i+1]]-self.abc[inp[i]]
                i += 2
            else:
                total += self.abc[inp[i]]
                i += 1
        return total
RomanNumerals = RomanNumerals()