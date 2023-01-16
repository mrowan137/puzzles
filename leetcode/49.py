"""
Runtime: 319 ms, faster than 5.03% of Python3 online submissions for Group Anagrams.
Memory Usage: 19.4 MB, less than 30.81% of Python3 online submissions for Group Anagrams.

given:
  - list of strings
  * can we assume all lower case? yes
  * what do we do with repeats? include it
goal:
  - group anagrams into the list

implementation:
  - map from vector to a group of anagrams
  - then go through list and add anagram to correct list
  - O(N*K) T, O(N*K) S, where K is the max length of string
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode(s):
            encoding = [0] * 26
            for c in s:
                encoding[ord(c) - ord("a")] += 1
            return tuple(encoding)

        anagram_groups = []
        anagram_group_to_index = {}
        for s in strs:
            if not encode(s) in anagram_group_to_index:
                anagram_groups.append([])
                anagram_group_to_index[encode(s)] = len(anagram_groups) - 1

            anagram_groups[anagram_group_to_index[encode(s)]].append(s)

        return anagram_groups


"""
Runtime: 417 ms, faster than 5.00% of Python3 online submissions for Group Anagrams.
Memory Usage: 19.4 MB, less than 20.99% of Python3 online submissions for Group Anagrams.
"""
from collections import Counter
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # cntr --> str
        dic = defaultdict(list)

        def string_to_tuple(cnt):
            res = [0] * 26
            for i in range(26):
                res[i] = cnt[chr(ord("a") + i)]
            return tuple(res)

        for s in strs:
            dic[string_to_tuple(Counter(s))].append(s)

        return [dic[k] for k in dic]


"""
Runtime: 159 ms, faster than 16.15% of Python3 online submissions for Group Anagrams.
Memory Usage: 19.1 MB, less than 25.41% of Python3 online submissions for Group Anagrams.
"""
# Using count to classify the words; two are 'the same' if sorted ~= have same count
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        def string_to_count(s):
            res = [0] * 26
            for c in s:
                res[ord(c) - ord("a")] += 1
            return res

        for s in strs:
            d[tuple(string_to_count(s))].append(s)

        return [v for v in d.values()]


"""
Runtime: 107 ms, faster than 50.02% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.2 MB, less than 78.82% of Python3 online submissions for Group Anagrams.
"""
# Map sorted(string) --> string
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(N k log k)
        # key : value  is sorted(word) : word
        d = defaultdict(list)
        for s in strs:  # ~O(N)
            d["".join(sorted(s))].append(
                s
            )  # ~O(k log k) where k is longest word

        return [v for v in d.values()]


"""
Runtime: 236 ms, faster than 5.03% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.7 MB, less than 63.52% of Python3 online submissions for Group Anagrams.
"""
from collections import defaultdict
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            ctr = Counter(s)
            ctr_k = "".join(
                [str(ctr[x]) + " " for x in "abcdefghijklmnopqrstuvwxyz"]
            )
            dic[ctr_k].append(s)

        return [v for v in dic.values()]
