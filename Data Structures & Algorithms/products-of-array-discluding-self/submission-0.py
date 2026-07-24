class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        # create left and right arrays of 1s 
        left = [1] * len_nums
        right = [1] * len_nums
        # iterate over left side starting from 1 (nothing left of 0)
        for i in range(1, len_nums):
            # the product of everything left of my neighbor, times my neighbour
            left[i] = left[i - 1] * nums[i - 1]
        # second-to-last index, index 0 is the last one processed, count downwards
        for i in range(len_nums - 2, -1, -1):
            # product right of my right-neighbor, times that neighbor
            right[i] = right[i + 1] * nums[i + 1]
        # Multiplies the two arrays position by position
        return [left[i] * right[i] for i in range(len_nums)]

        