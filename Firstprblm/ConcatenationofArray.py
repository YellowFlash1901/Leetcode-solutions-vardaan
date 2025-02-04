class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        copy = []
        copy = nums
        result = []
        for i in range(0,len(nums)):
            result.append(nums[i])
        for j in range(0, len(copy)):
            result.append(copy[j])
        
        return result