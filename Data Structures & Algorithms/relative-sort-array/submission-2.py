class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2Set = set(arr2)
        arr1Count = defaultdict(int)
        res = []
        end = []

        for num in arr1:
            if num not in arr2Set:
                end.append(num)
            else:
                arr1Count[num] += 1
        end.sort()

        for num in arr2:
            for i in range(arr1Count[num]):
                res.append(num)

        return res + end
        