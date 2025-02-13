'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
AND
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3575/
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Ensure nums length is between 0 and 100
        while True:
            if (0 <= len(nums) <= 100):
                break

        # Ensure num is between 0 and 50
        for num in nums:
            while True:
                if (0 <= num <= 50):
                    break

        # Ensure val is between 0 and 100
        while True:
            if (0 <= val <= 100):
                break

        k = 0
                
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1

        return k