class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [1] * n
        counter = 0
        # Contract: passes the number of players still in the game(n). Base case 
        #           n == 1 when a winner can be determined.
        def helper(n, i):
            nonlocal counter
            if n == 1:
                return
            if counter == 20:
                return
            else:
                counter += 1

            eliminate = False
            period = k - 1
            while eliminate is False:

                if not period and players[i]:
                    players[i] = 0
                    i = (i + 1) % len(players)
                    eliminate = True
                    while players[i] == 0:
                        i = (i + 1) % len(players)
                else:
                    i = (i + 1) % len(players)
                    period -= 1
                    while players[i] == 0:
                        i = (i + 1) % len(players)
                if counter == 20:
                    return
                else:
                    counter += 1

            helper(n-1, i)

        helper(n, 0)
        for i in range(len(players)):
            if players[i]:
                return i+1
