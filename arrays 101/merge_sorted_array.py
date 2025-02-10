'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
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
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1