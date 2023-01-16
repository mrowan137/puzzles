"""
Runtime: 88 ms, faster than 98.51% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.8 MB, less than 51.78% of Python3 online submissions for Top K Frequent Elements.
"""
# Complexity: O(N) on average, O(N^2) in the worst case
# Worst case attainable if you take r as the pivot at each step, then
# you do not cut the search space in half, but reduce by just one element
from itertools import chain
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We could use the Hoare's algorithms
        cnt = Counter(nums)
        unique = list(cnt.keys())

        def partition(l, r, pivot):
            pivot_idx = l
            unique[pivot], unique[r] = unique[r], unique[pivot]
            for i in range(l, r):
                if (
                    cnt[unique[r]] > cnt[unique[i]]
                ):  # pivot was swapped to right
                    unique[pivot_idx], unique[i] = unique[i], unique[pivot_idx]
                    pivot_idx += 1

            unique[r], unique[pivot_idx] = unique[pivot_idx], unique[r]
            return pivot_idx

        def quickselect(l, r, target):
            """
            place pivots into correct location until one
            pivot reaches the target distance from end
            """
            if l == r:
                return

            pivot = (l + r) // 2
            pivot = partition(l, r, pivot)

            if pivot == target:
                return  # done
            elif pivot < target:
                quickselect(pivot + 1, r, target)
            elif pivot > target:
                quickselect(l, pivot - 1, target)

        quickselect(0, len(unique) - 1, len(unique) - k)
        return unique[-k:]


"""
Runtime: 104 ms, faster than 43.60% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 20 MB, less than 7.06% of Python3 online submissions for Top K Frequent Elements.
"""
# O(N)
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = (
                unique[right],
                unique[pivot_index],
            )

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = (
                        unique[i],
                        unique[store_index],
                    )
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = (
                unique[store_index],
                unique[right],
            )

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            if left == right:
                return

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        quickselect(0, n - 1, n - k)
        return unique[n - k :]


# from itertools import chain
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # freqs can be in range [0, n]
#         freqs = [[] for _ in range(len(nums)+1)]
#         for num, freq in Counter(nums).items(): freqs[freq].append(num)
#         return list(chain(*freqs))[-k:]
