class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree: dict[str, int] = defaultdict(int)
        g: dict[str, List[int]] = defaultdict(list)
        answer = ""

        for word in words:
            for ch in word:
                indegree[ch] = 0
                g[ch] = []

        def lexical_comparison(word1: str, word2: str) -> tuple[str, str]:
            i = 0
            j = 0

            while i < len(word1) and j < len(word2):
                if word1[i] != word2[j]:
                    return (word1[i], word2[j])
                i += 1 
                j += 1
            
            if len(word1) > len(word2):
                return ("-1", "-1")
            else:
                return ("", "")

        for i in range(1, len(words)):
            u, v = lexical_comparison(words[i - 1], words[i])
            if u == "-1":
                return ""
            if u != "":
                indegree[v] += 1
                indegree[u] = 0 + indegree[u]
                g[u].append(v)

        queue = deque()

        for k, v in indegree.items():
            if indegree[k] == 0:
                queue.append(k)
        visited = 0
        while queue:
            node = queue.popleft()
            answer += node
            visited += 1
            for nei in g[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        if len(indegree) == visited:
            return answer
        else:
            return ""
        




        
        

        

