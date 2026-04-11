class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            length = r - l
            area = length * min(heights[l], heights[r])

            if area > max_area:
                max_area = area

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
            #print(f"(l, r): ({l}, {r})\nheights: {heights[l]}, {heights[r]}")

        return max_area
