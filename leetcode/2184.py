# Runtime: 569 ms (beats 97.79%)
# Memory: 14.2 MB (beats 99.26%)
from collections import defaultdict


class Solution:
    def buildWall(self, height, width, bricks):
        # hold all layers consistent with given bricks
        possibleLayers = []

        # build the first layer: currwidth 0, layer bitmask 0
        self.buildLayers(0, width, bricks, 0, possibleLayers)

        # dp[layer] to store number of ways to build to layer (at the current height)
        dp = {}

        # to track that, will need to know for a curr layer, what layer can go to
        # transitions[layer] is a list of layers we can go to from layer
        transitions = defaultdict(list)

        # initialize the ways to reach layer; for the first layer,
        # there's only 1 posible way for current layer
        for layer in possibleLayers:
            dp[layer] = 1

        # for each possible layer, compute the layers it could transition to
        # layer is encoded as binary
        for frm in possibleLayers:
            for to in possibleLayers:
                if (frm & to) == 0:
                    # only if no 1's lineup it is valid transition frm --> to
                    transitions[frm].append(to)

        # build from the top layer down
        # for each possible layer,
        while height > 1:
            dpNext = {}
            # iterate over possible layers, and possible transitions
            for nxt in possibleLayers:
                # sum up the number of ways you could get to that layer
                # it's sum over dp[prev], for prev in transitions[nxt]
                count = 0
                for prev in transitions[nxt]:
                    count = (count + dp[prev]) % 1000000007

                # I can reach nxt layer in count ways
                dpNext[nxt] = count

            # now dp is dpNext, dpNext is to be filled
            dp = dpNext
            height -= 1

        # the final result is the sum of total ways to reach each layer
        return sum(dp.values()) % 1000000007

    def buildLayers(self, currWidth, width, bricks, layerMask, l):
        for brick in bricks:
            if currWidth + brick == width:
                # we reached a full layer
                l.append(layerMask)
            elif currWidth + brick < width:
                # continue building, incorporate current knowledge to mask
                # the layer mask is a bitmask represent the layer;
                # given the current layer mask, the new one is the logial OR
                # of current bitmask, and place the next separator at brick
                self.buildLayers(
                    currWidth + brick,
                    width,
                    bricks,
                    layerMask | (1 << (currWidth + brick)),
                    l,
                )
