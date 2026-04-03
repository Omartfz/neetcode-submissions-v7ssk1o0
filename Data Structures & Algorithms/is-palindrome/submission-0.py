class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(ch.lower() for ch in s if ch.isalnum())
        return text == text[::-1]