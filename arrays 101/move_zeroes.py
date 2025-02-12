'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:
1 <= nums.length <= 10^4
-231 <= nums[i] <= 231 - 1
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Ensure nums length is between 1 and 10^4
        while True:
            if (1 <= len(nums) <= 10**4):
                break

        # Ensure num is between -2^31 and 2^31 - 1
        for num in nums:
            while True:
                if (-2**31 <= num <= 2**31 - 1):
                    break

        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index = non_zero_index + 1

        for i in range(non_zero_index, len(nums)):
            nums[i] = 0