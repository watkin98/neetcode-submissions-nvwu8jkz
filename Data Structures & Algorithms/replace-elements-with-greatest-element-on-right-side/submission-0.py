class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestElement = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            ithElement = arr[i]
            arr[i] = greatestElement

            if ithElement > greatestElement:
                greatestElement = ithElement

        return arr