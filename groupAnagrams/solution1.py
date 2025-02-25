from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts = defaultdict(list)
        for char in strs:
            dicts[''.join(sorted(char))].append(char)
        return dicts.values()