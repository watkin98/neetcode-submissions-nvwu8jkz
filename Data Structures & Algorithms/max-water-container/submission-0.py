class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l = 0
        r = 1

        for l in range(len(heights)):
            r = l+1

            while r < len(heights):
                length = r - l
                height = 0
                if heights[l] <= heights[r]:
                    height = heights[l]
                else:
                    height = heights[r]

                area = height * length

                if area > max_area:
                    max_area = area

                r += 1

        return max_area



