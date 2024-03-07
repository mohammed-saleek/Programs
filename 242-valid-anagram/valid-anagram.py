class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapper_one = {}
        mapper_two = {}
        if len(s) == len(t):
            #mapper one
            for letter in s:
                if letter in mapper_one:
                    mapper_one[letter] += 1
                else:
                    mapper_one[letter] = 1
            
            #mapper two
            for letter in t:
                if letter in mapper_two:
                    mapper_two[letter] += 1
                else:
                    mapper_two[letter] = 1
            
            if set(mapper_one.keys()) != set(mapper_two.keys()):
                return False
            
            for key in mapper_one:
                if mapper_one[key] != mapper_two[key]:
                    return False
            return True
        else:
            return False
        