class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        length = 0 # counter of sequence
        for n in set_nums: 
     	    if n-1 not in set_nums:
                length = 1 
                current = n +1
                while current in set_nums:
                    length += 1
                    current += 1 
                if length > longest:
                    longest = length
        return longest