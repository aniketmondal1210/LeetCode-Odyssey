class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        # Sort the three values
        x, y, z = sorted([a, b, c])
        # Original range (no operations)
        original_range = z - x
        # After replacing z with x + y:
        # New triple is (x, y, x+y)
        # New range = max(x, y, x+y) - min(x, y, x+y)
        # Since x, y are positive: min = x, max = x+y
        # New range = (x+y) - x = y
        # Note: if x+y < y (impossible for positive x), but x >= 0
        # So new range = y
        return min(original_range, y)
