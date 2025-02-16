'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
AND
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Ensure nums length is between 1 and 10^4
        while True:
            if (1 <= len(nums) <= 10**4):
                break

        # Ensure i is between -10^4 and 10^4
        for i in nums:
            if (-10**4 <= i <= 10**4):
                break

        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        index = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] ** 2
                left = left + 1
            else:
                result[index] = nums[right] ** 2
                right = right - 1
            index = index - 1

        return result