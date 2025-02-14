'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Ensure nums length is between 1 and 10^4
        while True:
            if (1 <= len(nums) <= 10**4):
                break

        # Ensure i is between -2^31 and 2^31 - 1
        for i in nums:
            while True:
                if (-2**31 <= i <= 2**31 - 1):
                    break

        third_distinct_maximum = set(nums)

        if len(third_distinct_maximum) < 3:
            return max(third_distinct_maximum)

        third_distinct_maximum.remove(max(third_distinct_maximum))
        third_distinct_maximum.remove(max(third_distinct_maximum))
        
        return max(third_distinct_maximum)