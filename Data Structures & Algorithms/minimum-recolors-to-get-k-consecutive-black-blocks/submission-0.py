class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L, R = 0, k - 1
        res = len(blocks)

        while R < len(blocks):
            whiteCount = 0
            for i in range(L, R+1):
                if blocks[i] == "W":
                    whiteCount += 1
            res = min(res, whiteCount)
            
            L += 1
            R += 1

        return res
            