"""
Runtime: 83 ms, faster than 41.64% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 14.2 MB, less than 5.86% of Python3 online submissions for Top K Frequent Words.
"""
# O(N) to build counter, O(log(k)) sorting potential words to add --> O(N log k)
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsToCount = Counter(words)
        res = []

        potentials = []
        for _ in range(k):
            if wordsToCount:
                m = max(
                    wordsToCount.items(), key=lambda wordToCount: wordToCount[1]
                )[1]
            if not potentials:
                while (
                    wordsToCount
                    and m
                    == max(
                        wordsToCount.items(),
                        key=lambda wordToCount: wordToCount[1],
                    )[1]
                ):
                    frequentWord = max(
                        wordsToCount.items(),
                        key=lambda wordToCount: wordToCount[1],
                    )
                    potentials.append(frequentWord[0])
                    del wordsToCount[frequentWord[0]]
            potentials = sorted(potentials)
            res.append(potentials[0])
            potentials.pop(0)

        return res
