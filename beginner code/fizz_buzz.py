'''
Link to the challenge: https://leetcode.com/problems/fizz-buzz/
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Constraints:
1 <= n <= 10^4
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Ensure n value is between 1 and 10^4
        while True:
            if (1 <= n <= 10**4):
                break
        
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        
        return answer