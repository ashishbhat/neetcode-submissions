class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                g[key].append(word)


        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, time = queue.popleft()
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                for nei in g[key]:
                    if nei == endWord:
                        return time + 1
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, time + 1))
                g[key] = []
        return 0

        

                

