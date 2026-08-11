class Solution:
    def trap(self, height: List[int]) -> int:
        # Find first elevation
        L = 0
        while height[L] == 0:
            L += 1
        
        # Setup R pointer after first elevation
        R = L + 1
        resArea = 0

        while R < len(height):

            # Search for an instance where the R pointer/pillar is less than the adjacent L pointer/pillar
            while R < len(height) and height[R] >= height[L]:
                L += 1
                R += 1
            # Pointer/pillar for resovoir
            R += 1
            
            if R >= len(height):
                break
            # Translate R pointer/pillar to find maximum possible area relative to L pointer/pillar
            while R < len(height) and height[R] < height[L]:
                R += 1

            if R >= len(height):
                break
            # Calculate area of current resovoir, then add it to resArea
            curArea = 0
            for i in range(L+1, R):
                curArea += height[L] - height[i]
            resArea += curArea

            # Setup new possible resovoir at R pointer/pillar
            L = R
            R += 1

        return resArea