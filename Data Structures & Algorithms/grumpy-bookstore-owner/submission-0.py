class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxCustomers = 0
        L, R = 0, minutes - 1
        L_max, R_max = 0, minutes - 1
        curCustomers = sum(customers[:minutes-1])

        while R < len(customers):
            curCustomers += customers[R]
            if curCustomers > maxCustomers:
                maxCustomers = curCustomers
                L_max = L
                R_max = R
            curCustomers -= customers[L]

            L += 1
            R += 1

        remainingCustomers = customers[0:L_max] + customers[R_max+1:]
        remainingGrumpy = grumpy[0:L_max] + grumpy[R_max+1:]

        for i in range(len(remainingCustomers)):
            if remainingGrumpy[i] == 0:
                maxCustomers += remainingCustomers[i]

        return maxCustomers


        
