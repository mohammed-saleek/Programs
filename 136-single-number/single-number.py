class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapper = {}
        for index, nums in enumerate(nums):
            if nums in mapper:
                mapper[nums] += 1
            elif nums not in mapper:
                mapper[nums] = 1
        # for key,value in mapper.items():
        #     if value == 1:
        #         unique_number = key
        unique_number = next((key for key,value in mapper.items() if value == 1), None)
        return unique_number