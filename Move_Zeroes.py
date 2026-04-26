"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 0
        n = len(nums)

        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        return nums