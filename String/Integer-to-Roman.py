class Solution:
    def intToRoman(self, num: int) -> str:
        intToRoman_map = {
            1: "I", 4: "IV", 5: "V", 9: "IX",
            10: "X", 50: "L", 40: "XL", 90: "XC",
            100: "C", 400: "CD", 500: "D", 900: "CM",
            1000: "M"
        }

        ans = ""

        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                ans += intToRoman_map[n]
                num -= n
        
        return ans       

        # intToRoman_map = [
        # (1000, 'M'),
        # (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
        # (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        # (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        # ]

        # ans = ""

        # for (value, roman) in intToRoman_map:
        #     while value <= num:
        #         ans += roman
        #         num -= value
        
        # return ans