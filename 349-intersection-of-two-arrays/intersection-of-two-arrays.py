class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # unique_list = []
        # for number in nums1:
        #     if number in nums2:
        #         unique_list.append(number)
        # response = list(set(unique_list))
        # return response
        unique_list = set([x for x in nums1 if x in nums2])
        return unique_list
        
