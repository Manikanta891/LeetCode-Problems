# Problem:
# Given a string of digits, return all possible letter combinations that the number could represent,
# based on the classic phone keypad mapping (e.g., '2' -> 'abc', '3' -> 'def', etc.).

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: if input is empty, return an empty list
        if not digits:
            return []

        # Mapping of digits to letters (index 0 and 1 are empty strings)
        data = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        # Result list to store all combinations
        res = []

        # Helper function to build combinations recursively
        def helper(word, pos):
            # If we've reached the end of the input digits, add the formed word to result
            if pos == len(digits):
                res.append(word)
                return

            # Get the corresponding letters for the current digit and recurse
            for ch in data[int(digits[pos])]:
                helper(word + ch, pos + 1)

        # Start backtracking from the first digit
        helper("", 0)
        return res
