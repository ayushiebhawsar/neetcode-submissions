class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaned = ''.join([wrd for wrd in s.lower() if wrd.isalnum()])
        # return cleaned[::-1] == cleaned

        s = ''.join([wrd for wrd in s.lower() if wrd.isalnum()])
        left,right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
        