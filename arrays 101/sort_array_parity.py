'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Ensure nums length is between 1 and 5000
        while True:
            if (1 <= len(nums) <= 5000):
                break

        # Ensure i is between 0 and 5000
        for i in nums:
            while True:
                if (0 <= i <= 5000):
                    break

        left = 0
        right = len(nums) - 1

        while left < right:
            while left < right and nums[left] % 2 == 0:
                left = left + 1
                
            while left < right and nums[right] % 2 != 0:
                right = right - 1
                
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left = left + 1 
                right = right - 1

        return nums