'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
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
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Ensure nums1 length is equal to m + n
        while True:
            if len(nums1) == m + n:
                break

        # Ensure nums2 length is equal to n
        while True:
            if len(nums2) == n:
                break

        # Ensure m and n is between 0 and 200
        while True:
            if (0 <= m <= 200 and 0 <= n <= 200):
                break

        # Ensure m + n is between 1 and 200
        while True:
            if (1 <= m + n <= 200):
                break

        # Ensure nums1 and nums2 is between -10^9 and 10^9
        for num in nums1:
            while True:
                if (-10**9 <= num <= 10**9):
                    break
        for num in nums2:
            while True:
                if (-10**9 <= num <= 10**9):
                    break

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i - 1
            else:
                nums1[k] = nums2[j]
                j = j - 1
            k = k - 1

        while j >= 0:
            nums1[k] = nums2[j]
            j = j - 1
            k = k - 1