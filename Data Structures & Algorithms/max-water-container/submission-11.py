class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_area = 0

        while l < r: 
            length = r - l
            height = 0

            if heights[l] <= heights[r]:
                height = heights[l]
            else:
                height = heights[r]

            area = length * height

            if area > max_area:
                max_area = area

            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -= 1

            #print(f"(l, r): ({l}, {r})")


        return max_area