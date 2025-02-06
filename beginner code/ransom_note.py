'''
Link to the challenge: https://leetcode.com/problems/ransom-note/description/
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Ensure both ransomNote and magazine length are between 1 and 10^5
        while True:
            if (1 <= len(ransomNote) <= 10**5 and 1 <= len(magazine) <= 10**5):
                break

        # Ensure both ransomNote and magazine have only lowercase letters
        while True:
            if (ransomNote.islower() and magazine.islower()):
                break

        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True