'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
Given an array nums of integers, return how many of them contain an even number of digits.

Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Ensure nums length is between 1 and 500
        while True:
            if (1 <= len(nums) <= 500):
                break

        count = 0

        for i in nums:
            # Ensure nums[i] is between 1 and 10^5
            while True:
                if (1 <= i <= 10**5):
                    break

            if len(str(i)) % 2 == 0:
                count = count + 1

        return count