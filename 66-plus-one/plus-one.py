class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_str = ('').join(str(number) for number in digits)
        result = int(digits_str) + 1
        result_list = [int(num) for num in str(result)]
        return result_list