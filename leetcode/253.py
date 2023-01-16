"""
Runtime: 84 ms, faster than 25.31% of Python3 online submissions for Meeting Rooms II.
Memory Usage: 17.6 MB, less than 23.20% of Python3 online submissions for Meeting Rooms II.
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # open up a queue when start is before all ends
        # if start after end for some interval, add to queue (closest)
        # ===========
        #        ===
        #          ===
        # dic tracks the end for each queue
        d, res = {0: -float("inf")}, 0

        # sort because of case like this:
        #      ====
        # ==
        # this will require two streams but only need one:
        # ==   ====
        # sorting by starte time ensures no interval can
        # end before what we currently have in the queue
        intervals = sorted(intervals, key=lambda x: x[0])

        for i in intervals:
            s, e = i
            if all([s < v for v in d.values()]):
                # open a new queue
                d[len(d)] = e
            else:
                # find d with min(s - d[k]) --> update with new end
                v_max = max([v for v in d.values() if v <= s])
                d_rev = {v: k for k, v in d.items()}
                k_closest = d_rev[v_max]
                d[k_closest] = e

        return len(d)
