class Solution:
    def firstPalindrome(self, words):
        def is_palindrome(s: str) -> bool:
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""

#Below version completly turn the string into reverse and compare it with original string
#But the above version is more efficient as it only checks characters from both ends towards the center
#When the characters from both ends are not equal it returns false instantly

# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
        
#         for string in words:
#             if string==string[::-1]:
#                 return string
#         return ""