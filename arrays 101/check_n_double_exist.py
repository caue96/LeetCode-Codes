'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Constraints:
2 <= arr.length <= 500
-103 <= arr[i] <= 103
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Ensure arr length is between 2 and 500
        while True:
            if (2 <= len(arr) <= 500):
                break

        # Ensure i is between -10^3 and 10^3
        for i in arr:
            while True:
                if (-10**3 <= i <= 10**3):
                    break

        search = set()
        
        for j in arr:
            if 2 * j in search or (j % 2 == 0 and j // 2 in search):
                return True
            search.add(j)

        return False