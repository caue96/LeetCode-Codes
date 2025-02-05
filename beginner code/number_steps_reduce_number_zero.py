'''
Link to the challenge: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Constraints:
0 <= num <= 10^6
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Ensure num value is between 0 and 10^6
        while True:
            if (0 <= num <= 10**6):
                break

        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            steps = steps + 1

        return steps