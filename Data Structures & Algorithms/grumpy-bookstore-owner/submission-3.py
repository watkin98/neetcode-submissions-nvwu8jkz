class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        L = 0
        dissatisfiedWindowSum = maxDissatisfiedWindowSum = 0
        satisfiedSum = 0

        for R in range(len(customers)):
            if grumpy[R]:
                dissatisfiedWindowSum += customers[R]
            else:
                satisfiedSum += customers[R]

            if R - L + 1 > minutes:
                if grumpy[L]:
                    dissatisfiedWindowSum -= customers[L]
                L += 1

            maxDissatisfiedWindowSum = max(maxDissatisfiedWindowSum, dissatisfiedWindowSum)

        return satisfiedSum + maxDissatisfiedWindowSum
