class Solution:
    def myHash(self,s: str) -> tuple:
        freq = [0]*26
        h = ""
        for ch in s:
            freq[ord(ch) - 97] += 1
        return tuple(freq)        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            h = self.myHash(s)
            anagrams[h].append(s)

        return list(anagrams.values())


        