class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                g[key].append(word)


        queue = deque()
        visited = set()

        for i in range(len(beginWord)):
            key = beginWord[:i] + "*" + beginWord[i+1:]
            visited.add(key)
            queue.append((key, 2))
        print(queue)

        while queue:
            word, t = queue.popleft()
            print(t)
            for w in g[word]:
                print(w)
                if w == endWord:
                    return t
                else:
                    for i in range(len(w)):
                        key = w[:i] + "*" + w[i+1:]
                        if key not in visited:
                            visited.add(key)
                            queue.append((key, t+1))
        return 0

                

