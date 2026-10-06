class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[j].isalnum():
                if j == 0:
                    return True
                j -= 1
            while not s[i].isalnum():
                i += 1
            if s[i].upper() != s[j].upper():
                return False
            else:
                j -= 1
                i += 1
                continue
        return True