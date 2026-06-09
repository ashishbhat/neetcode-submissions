class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        result = strs[0]

        for s in strs[1:]:
            for i in range(len(result)):
                if s[i] != result[i]:
                    result = result[0:i]
                    break
        
        return result if result else ""