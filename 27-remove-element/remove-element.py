class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_copy = []
        # nums_copy = nums.copy()
        for item in nums:
            nums_copy.append(item)
        for index,value in enumerate(nums_copy):
            if value == val:
                nums.remove(value)
        return len(nums)

        