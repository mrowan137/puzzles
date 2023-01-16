"""
There are N dishes in a row on a kaiten belt, with the ith dish being of type
D_i. Some dishes may be of the same type as one another. You're very hungry, but
you'd also like to keep things interesting. The N dishes will arrive in front of
you, one after another in order, and for each one you'll eat it as long as it
isn't the same type as any of the previous KK dishes you've eaten. You eat very
fast, so you can consume a dish before the next one gets to you. Any dishes you
choose not to eat as they pass will be eaten by others. Determine how many
dishes you'll end up eating.
"""
from typing import List
from collections import deque
from collections import defaultdict


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    res = 0
    d = deque()
    cnt = defaultdict(int)
    for i in range(N):
        if cnt[D[i]] == 0:
            res += 1
            d.append(D[i])
            cnt[D[i]] += 1
        if len(d) > K:
            cnt[d.popleft()] -= 1

    return res
