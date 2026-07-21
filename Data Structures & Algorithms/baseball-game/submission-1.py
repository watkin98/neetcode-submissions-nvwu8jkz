class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreTracker = []

        for i in range(len(operations)):
            if operations[i] == '+':
                num1 = scoreTracker[len(scoreTracker) - 1]
                num2 = scoreTracker[len(scoreTracker) - 2]
                scoreTracker.append(num1 + num2)
            elif operations[i] == 'D':
                double = scoreTracker[len(scoreTracker) - 1] * 2
                scoreTracker.append(double)
            elif operations [i] == 'C':
                scoreTracker.pop()
            else:
                num = int(operations[i])
                scoreTracker.append(num)

            print(operations[i])
            print(scoreTracker)
            print()
        
        sum = 0
        for num in scoreTracker:
            sum += num

        return sum