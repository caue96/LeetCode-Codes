'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Ensure arr length is between 1 and 10^4
        while True:
            if (1 <= len(arr) <= 10**4):
                break
        
        # Ensure num is between 1 and 10^5
        for num in arr:
            while True:
                if (1 <= num <= 10**5):
                    break
        
        n = len(arr)
        max_right = -1
        
        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)
        
        return arr