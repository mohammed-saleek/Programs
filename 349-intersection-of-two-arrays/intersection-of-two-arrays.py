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
        # unique_list = set([x for x in nums1 if x in nums2])
        # return unique_list
        # taking two hashmaps to store the each value and its count
        hashMap1 = defaultdict(int)
        hashMap2 = defaultdict(int)
        # a list to store the value
        answerList = []

        for i in nums1:
            hashMap1[i] = hashMap1[i] + 1

        for i in nums2:
            hashMap2[i] = hashMap2[i] + 1

        # for each value in hashMap1 , if that is present in hashMap2, we append it to the answerList
        for key in hashMap1:
            if key in hashMap2:
                answerList.append(key)
        return answerList
