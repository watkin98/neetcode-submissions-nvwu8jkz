class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, left, right):
        if left >= right:
            return

        m = (right + left) // 2

        self.mergeSort(nums, left, m)
        self.mergeSort(nums, m+1, right)
        self.merge(nums, left, m, right)

    def merge(self, nums, left, mid, right):
        leftArray, rightArray = nums[left:mid+1], nums[mid+1:right+1]
        i, L, R = left, 0, 0

        while L < len(leftArray) and R < len(rightArray):
            if leftArray[L] <= rightArray[R]:
                nums[i] = leftArray[L]
                L += 1
            else:
                nums[i] = rightArray[R]
                R += 1
            i += 1

        while L < len(leftArray):
            nums[i] = leftArray[L]
            L += 1
            i += 1
        while R < len(rightArray):
            nums[i] = rightArray[R]
            R += 1
            i += 1
        