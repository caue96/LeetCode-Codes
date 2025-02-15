'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Pass nums length to n, to make the contraint n == nums.length true
        n = len(nums)
        
        # Ensure n value is between 1 and 10^5
        while True:
            if (1 <= n <= 10**5):
                break
        
        # Ensure num value is between 1 and (n or nums.length)
        for num in nums:
            while True:
                if (1 <= num <= n):
                    break
        
        for num in nums:
            index = abs(num) - 1
            
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        disappeared_numbers = []
        for i in range(n):
            if nums[i] > 0:
                disappeared_numbers.append(i + 1)
        
        return disappeared_numbers