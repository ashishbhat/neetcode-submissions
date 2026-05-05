class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            encoding += "#"+str(len(s))+"#"+s
        return encoding


    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        result = []
        while i < len(s):
            i = i+1
            n = ""

            while s[i] != '#':
                n += s[i]
                i += 1
            k = int(n)
            i += 1
            result.append(s[i:i+k])
            i += k
        return result
            
            

