'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 9
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # Ensure arr lenght is between 1 and 10^4
        while True:
            if (1 <= len(arr) <= 10**4):
                break
        
        # Ensure num is between 0 and 9
        for num in arr:
            if (0 <= num <= 9):
                break
        
        n = len(arr)
        i = 0

        while i < n:
            if arr[i] == 0:
                for j in range(n - 1, i, -1):
                    arr[j] = arr[j - 1]

                if i + 1 < n:
                    arr[i + 1] = 0

                i = i + 2

            else:
                i = i + 1