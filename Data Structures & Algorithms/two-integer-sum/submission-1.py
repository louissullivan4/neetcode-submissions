class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [2, 1, 2, 3]  result = 4 output [0, 2]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

# Addition of two indexes in a list that equal a target
# The two indexes are not the same