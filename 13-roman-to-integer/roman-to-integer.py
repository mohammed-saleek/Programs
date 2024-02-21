class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapper = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        result = 0
        sub_value = 0
        if "IV" in s or "IX" in s:
            sub_value = 2 + sub_value
            print("oh yesssssssss")
        if "XL" in s or "XC" in s:
            sub_value = 20 + sub_value
        if "CD" in s or "CM" in s:
            sub_value = 200 + sub_value
        for roman_number in s:
            result = mapper[roman_number] + result
        result = result - sub_value
        return result
        