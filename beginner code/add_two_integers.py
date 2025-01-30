'''
Link to the challenge: https://leetcode.com/problems/add-two-integers/description/
Given two integers num1 and num2, return the sum of the two integers.

Constraints:
-100 <= num1, num2 <= 100
'''
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # Constrain num1 to be equal to or bigger than -100
        while True:
            if num1 >= -100:
                break

        # Constrain num2 to be equal to or less than 100
        while True:
            if num2 <= 100:
                break

        return num1 + num2