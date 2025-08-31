import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag_len_rect = 0
        rect_area = 0
        for len,breadth in dimensions:
            max_diag_len_rect = math.sqrt(len**2 + breadth**2)
            max_rect_area = len * breadth
            if max_diag_len_rect > diag_len_rect:
                diag_len_rect = max_diag_len_rect
                rect_area = max_rect_area
            elif max_diag_len_rect == diag_len_rect:
                rect_area = max(max_rect_area,rect_area)
        return rect_area
