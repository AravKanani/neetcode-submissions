class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        for letter in s:
            count_s[letter] = count_s.get(letter, 0) + 1
        
        count_t = {}
        for letter in t:
            count_t[letter] = count_t.get(letter, 0) + 1

        return count_t == count_s





















































































