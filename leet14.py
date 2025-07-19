class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        prefix = strs[0]
    
        for word in strs[1:]:
            temp_prefix = ""
            for j in range(min(len(prefix), len(word))):
                if prefix[j] == word[j]:
                    temp_prefix += prefix[j]
                else:
                    break
            prefix = temp_prefix
            if not prefix:
                return ""
        return prefix
