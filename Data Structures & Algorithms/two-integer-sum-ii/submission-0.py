class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                print(1)
                l += 1
            elif sum > target:
                print(2)
                r -= 1
            else:
                print(3)
                return [l+1, r+1]