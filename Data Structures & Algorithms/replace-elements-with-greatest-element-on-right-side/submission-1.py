class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Store the last element in the arr in a greatestNum variable. 
        # Iterate through the arr backwards. Store the encountered element 
        # and replace it with greatestNum. Replace greatestNum with the element
        # if it is greater. Return arr after iteration

        greatestNum = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1

        for i in range(len(arr) - 2, -1, -1):
            num = arr[i]
            arr[i] = greatestNum
            greatestNum = max(greatestNum, num)

        return arr
         