class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while start < end:
            csum = numbers[end] + numbers[start]

            if csum > target:
                end -= 1
            elif csum < target:
                start += 1
            else:
                return [start + 1, end + 1]
        
        return []
