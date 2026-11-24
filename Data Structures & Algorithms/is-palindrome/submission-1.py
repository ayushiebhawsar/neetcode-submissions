class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join([wrd for wrd in s.lower() if wrd.isalnum()])
        return cleaned[::-1] == cleaned
        