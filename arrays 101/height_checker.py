'''
Link to the challenge: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Constraints:
1 <= heights.length <= 100
1 <= heights[i] <= 100
'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Ensure heights length is between 1 and 100
        while True:
            if (1 <= len(heights) <= 100):
                break

        # Ensure height is between 1 and 100
        for height in heights:
            while True:
                if (1 <= height <= 100):
                    break

        expected = sorted(heights)
        mismatch_count = 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count = mismatch_count + 1

        return mismatch_count