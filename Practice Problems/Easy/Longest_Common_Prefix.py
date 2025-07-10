class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first word as the prefix
        prefix = strs[0]

        # Compare prefix with every word in the list
        for word in strs[1:]:
            while not word.startswith(prefix):
                # Chop off last character until match is found
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix