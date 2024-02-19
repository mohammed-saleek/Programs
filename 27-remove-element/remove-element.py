class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # nums_copy = nums.copy()
        nums_copy = []
        for i in nums:
            nums_copy.append(i)
        for index,value in enumerate(nums_copy):
            if value == val:
                nums.remove(value)
        return len(nums)

        