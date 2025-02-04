'''
Link to the challenge: https://leetcode.com/problems/running-sum-of-1d-array/
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Ensure the size of nums is bigger or equal to 1 and less or equal to 1000
        while True:
            if (1 <= len(nums) <= 1000):
                break

        # Ensure the value of nums[i] is bigger or equal to -10^6 and less or equal to 10^6
        for num in nums:
            if (-10**6 <= num <= 10**6):
                break

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        return nums