class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        # for num2 in arr2:
        #     for i, num1 in enumerate(arr1):
        #         if num1 == num2:
        #             temp = arr1.pop(i)
        #             res.append(temp)
        for num2 in arr2:
            i = 0
            while i < len(arr1):
                if arr1[i] == num2:
                    temp = arr1.pop(i)
                    res.append(temp)
                else:
                    i += 1

        arr1.sort()
        return res + arr1