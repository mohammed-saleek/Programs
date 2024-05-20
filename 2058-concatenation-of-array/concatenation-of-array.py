class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = []
        # for i in range(2):
        #     for index in range(len(nums)):
        #         result.append(nums[index])
        # return result
        result = []
        l2 = []
        for index in range(len(nums)):
            result.append(nums[index])
            l2.append(nums[index])
        result.extend(l2)
        return result
        