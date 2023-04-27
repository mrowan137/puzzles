"""
Runtime: 52 ms (Beats 9.49%)
Memory: 16.3 MB (Beats 39.65%)
"""

# One-liner
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(", "").replace(")", "")
