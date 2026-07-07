class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        s = Counter(t)
        if c == s:
            return True
        return False