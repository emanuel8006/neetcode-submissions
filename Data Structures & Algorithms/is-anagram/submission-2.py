from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_ct = {}
        t_ct = {}
        for i in range(len(s)):
            s_ct[s[i]] = 1 + s_ct.get(s[i], 0)
            t_ct[t[i]] = 1 + t_ct.get(t[i], 0)
        return s_ct == t_ct