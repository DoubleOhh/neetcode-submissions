class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in numbers:
                return [numbers[diff],i]
            else:
                numbers[num]= i