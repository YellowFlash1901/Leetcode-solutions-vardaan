class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = {}
        for num in nums:
            if num in ans:
                ans[num] += 1  # Increment the value if the key already exists
            else:
                ans[num] = 1  # Initialize key with value 1 if not found

        
        return max(ans, key=ans.get)
