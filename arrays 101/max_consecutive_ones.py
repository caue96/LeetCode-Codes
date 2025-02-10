'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Ensure nums length between 1 and 105
        while True:
            if (1 <= len(nums) <= 10**5):
                break

        max_count = 0
        current_count = 0

        for i in nums:
            # Ensure nums[i] is 0 or 1
            while True:
                if i in {0, 1}:
                    break

            if i == 1:
                current_count = current_count + 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count