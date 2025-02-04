class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first_string = sorted(list(s))
        second_string = sorted(list(t))

        if first_string == second_string:
            return True
        else:
            return False

