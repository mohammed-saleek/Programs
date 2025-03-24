class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mapper = {}
        for number in nums:
            if number in mapper:
                mapper[number] = mapper[number] + 1
            else:
                mapper[number] = 1
        top_k_keys = [key for key, value in sorted(mapper.items(), key=lambda item: item[1], reverse=True)[:k]]
        return top_k_keys