"""
Runtime: 484 ms, faster than 34.52% of Python3 online submissions for Word Ladder.
Memory Usage: 15.2 MB, less than 79.71% of Python3 online submissions for Word Ladder.
"""
from collections import deque


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        # BFS strategy
        # q stores word and ladder length to that word
        # while there are words to explore:
        #     take word, length from the queue
        #         exit condition: if word is endWord, return length
        #     consider all one char changes from the word
        #     if change is in wordlist, remove change and append to q
        wordList = set(wordList)
        q = collections.deque([[beginWord, 1]])
        while q:
            w, n = q.popleft()
            print(w)
            if w == endWord:
                return n

            for i in range(len(w)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nxt = w[:i] + c + w[i + 1 :]
                    if nxt in wordList:
                        wordList.remove(nxt)
                        q.append([nxt, n + 1])

        return 0


# TLE -- BRUTE FORCE
from collections import deque


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        # Idea: work backwards
        # root = endWord
        # n = 0, the number of steps
        # seen = set(), contains the words seen so far
        # while beginWord not seen:
        #    - consider all unseen words that differ by one word
        #    - add these to seen
        #    - recurse on these new words
        def transforms(w1, w2):
            if len(w1) != len(w2):
                return False

            strikes = 1
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    strikes -= 1

            return strikes >= 0

        wordsList = set(wordList)
        seen = set()
        q = deque([[beginWord]])  # words to consider at this step
        n = 1
        while endWord not in seen and q:
            curr = q.pop()
            new = deque()
            while curr:
                c = curr.pop()
                added = []
                for w in wordsList:
                    if w not in seen and transforms(c, w):
                        new.append(w)
                        seen.add(w)
                        added.append(w)

                for w in added:
                    wordsList.remove(w)

            if new:
                q.append(new)
            n += 1

        return n if q and endWord in q[0] else 0
