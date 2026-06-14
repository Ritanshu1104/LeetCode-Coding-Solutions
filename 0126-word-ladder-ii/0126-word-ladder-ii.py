from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        L = len(beginWord)

        patterns = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(L):
                patterns[word[:i] + "*" + word[i+1:]].append(word)

        parents = defaultdict(list)
        dist = {beginWord: 0}

        q = deque([beginWord])

        while q:
            word = q.popleft()

            if word == endWord:
                break

            for i in range(L):
                pat = word[:i] + "*" + word[i+1:]

                for nei in patterns[pat]:
                    if nei not in dist:
                        dist[nei] = dist[word] + 1
                        parents[nei].append(word)
                        q.append(nei)
                    elif dist[nei] == dist[word] + 1:
                        parents[nei].append(word)

        if endWord not in dist:
            return []

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for p in parents[word]:
                dfs(p, path + [p])

        dfs(endWord, [endWord])
        return ans