class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2Set = set(arr2)
        numCount = defaultdict(int)
        end = []

        for num in arr1:
            if num not in arr2Set:
                end.append(num)
            else:
                numCount[num] += 1

        res = []

        for num in arr2:
            for _ in range(numCount[num]):
                res.append(num)

        end.sort()
        return res + end
