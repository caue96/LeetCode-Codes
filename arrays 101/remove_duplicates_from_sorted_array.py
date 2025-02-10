'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Constraints:
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Ensure nums lenght is between 1 and 3 * 10^4
        while True:
            if (1 <= len(nums) <= 3 * 10**4):
                break
        
        # Ensure num is between -100 and 100
        for num in nums:
            while True:
                if (-100 <= num <= 100):
                    break
        
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k = k + 1
        
        return k