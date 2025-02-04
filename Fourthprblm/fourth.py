class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = {}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if complement in ans:
                return ans[complement], i
            
            ans[nums[i]] = i