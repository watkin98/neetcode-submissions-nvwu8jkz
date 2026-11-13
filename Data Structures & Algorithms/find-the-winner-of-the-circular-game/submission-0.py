class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [1] * n

        def helper(pos, elim):
            if elim == n-1:
                return

            count = k
            while True:
                if players[pos]:
                    count -= 1
                    if count == 0:
                        players[pos] = 0
                        break
                pos = (pos + 1) % n

            helper((pos + 1) % n, elim + 1)

        helper(0, 0)

        for i in range(len(players)):
            if players[i]:
                return i + 1