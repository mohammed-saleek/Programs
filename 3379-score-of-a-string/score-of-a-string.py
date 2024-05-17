class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for index in range(len(s)-1):
            result = result + abs(ord(s[index]) - ord(s[index+1]))
        return result
