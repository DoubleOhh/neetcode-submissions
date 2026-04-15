class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        test1 = Counter(s)
        test2 = Counter(t)

        if test1 == test2:
            return True
        return False
