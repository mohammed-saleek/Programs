class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = 0
        mapper = {
            "--X":-1,
            "X++":1,
            "++X":1,
            "X--":-1
        }
        for operation in operations:
            result = result + mapper[operation]
        return result