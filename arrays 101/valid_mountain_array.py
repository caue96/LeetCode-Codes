'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Ensure arr length is between 1 and 10^4
        while True:
            if (1 <= len(arr) <= 10**4):
                break
        
        # Ensure num is between 0 and 10^4
        for num in arr:
            while True:
                if (0 <= num <= 10**4):
                    break
        
        n = len(arr)
        if n < 3:
            return False
        
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i = i + 1
        
        if i == 0 or i == n - 1:
            return False
        
        while i + 1 < n and arr[i] > arr[i + 1]:
            i = i + 1
        
        return i == n - 1