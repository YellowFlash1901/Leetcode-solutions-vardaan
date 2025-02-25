from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts = defaultdict(list)
        for char in strs:
            lst = [0]*26
            for word in char:
                lst[ord(word)-ord('a')] +=1
            lst = tuple(lst)
            dicts[lst].append(char)
        return dicts.values()