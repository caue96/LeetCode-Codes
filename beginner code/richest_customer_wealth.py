'''
Link to the challenge: https://leetcode.com/problems/richest-customer-wealth/
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Constraints:
m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        # Ensure the number of costumers is bigger or equal to 1 and less or equal to 50
        while True:
            if (1 <= m <= 50):
                break
            
        n = len(accounts[0])
        # Ensure the number of banks is bigger or equal to 1 and less or equal to 50 
        while True:    
            if (1 <= n <= 50):
                break
        
        # Ensure the amount of money in an account is bigger or equal to 1 and less or equal to 100
        for i in range(m):
            for j in range(n):
                while True:
                    if (1 <= accounts[i][j] <= 100):
                        break
        
        max_wealth = 0
        # Calculate the wealth of each customer
        for customer in accounts:
            wealth = sum(customer)
            if wealth > max_wealth:
                max_wealth = wealth
        
        return max_wealth