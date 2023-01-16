"""
Runtime: 456 ms, faster than 93.37% of Python3 online submissions for Best Sightseeing Pair.
Memory Usage: 19.9 MB, less than 56.25% of Python3 online submissions for Best Sightseeing Pair.
"""
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Idea: iterate through array, tracking the 'best' value seen
        # so far; best_value = max(v, best_value).  The answer is almost
        # for v in values:
        #     res = max(res, best_value + v)
        #     best_value = max(best_value, v)
        # but it needs to be modified; best_value gets a -1 because values
        # get further away as we iterate through the array, affecting the score
        best_score = 0
        i = 0 # index of pair member to left
        for j in range(1, len(values)):
            # best score is either prev best score, or best score given new val
            best_score = max(best_score, values[j] + values[i] - (j - i))
            
            # update the prev best 
            if values[i] - (j - i) < values[j]: i = j
                
        return best_score
    
"""
Runtime: 474 ms, faster than 74.21% of Python3 online submissions for Best Sightseeing Pair.
Memory Usage: 19.8 MB, less than 57.41% of Python3 online submissions for Best Sightseeing Pair.
"""
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_score = 0
        best_value_so_far = 0
        
        for v in values:
            best_score = max(best_score, best_value_so_far + v)
            best_value_so_far = max(best_value_so_far, v) - 1
            
        return best_score

    
