class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]  # assume first word is prefix
        
        for word in strs[1:]:
            # shrink prefix until it matches
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # remove last char
                if not prefix:
                    return ""
        
        return prefix