class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxCustomers = 0
        L, R = 0, minutes - 1
        L_max, R_max = 0, minutes - 1
        disatisfiedCustomers = customers[0] if R - L - 1 == 0 and grumpy[0] == 1 else 0
        for i in range(R-1):
            if grumpy[i] == 1:
                disatisfiedCustomers += customers[i]

        while R < len(customers):
            if grumpy[R] == 1:
                disatisfiedCustomers += customers[R]
            if disatisfiedCustomers > maxCustomers:
                maxCustomers = disatisfiedCustomers
                L_max = L
                R_max = R
            if grumpy[L] == 1:
                disatisfiedCustomers -= customers[L]
            L += 1
            R += 1

        for i in range(L_max, R_max+1):
            grumpy[i] = 0

        res = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]

        return res


        
