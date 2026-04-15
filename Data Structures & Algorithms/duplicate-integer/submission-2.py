class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non = set()
        for num in nums:
            if num in non:
                return True
            else:
                non.add(num)
        return False