class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                threesum = num + nums[j] + nums[k]

                if threesum < 0:
                    j += 1
                elif threesum > 0:
                    k -= 1
                else:
                    output.append([num, nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return output
        