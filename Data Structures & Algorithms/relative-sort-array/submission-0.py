class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        i1 = 0

        for num in arr2:
            while i1 < len(arr1):
                if arr1[i1] == num:
                    temp = arr1.pop(i1)
                    res.append(temp)
                else:
                    i1 += 1
            i1 = 0

        arr1.sort()

        return res + arr1