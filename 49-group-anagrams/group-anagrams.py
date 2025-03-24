class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create a mapper 
        mapper = {}
        for index, word in enumerate(strs):
            checker = ''.join(sorted(word))
            if checker in mapper:
                mapper[checker].append(index)
            else:
                mapper[checker] = [index]
        
        # Set the output using the word mapper
        result = []
        for key, value in mapper.items():
            sub_result = [strs[index] for index in value]
            result.append(sub_result)
        return (result)