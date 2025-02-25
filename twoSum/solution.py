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
            print("complement",complement)
            if complement in ans:
                return ans[complement], i
            
            ans[nums[i]] = i
            print("key",nums[i],"value",i,"ans",ans)