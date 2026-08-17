class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = len(nums1) - 1

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                print(1)
                nums1[r] = nums1[m-1]
                m -= 1
            else:
                print(2)
                nums1[r] = nums2[n-1]
                n -= 1
            r -= 1

        while m > 0:
            print(3)
            nums1[r] = nums1[m-1]
            m -= 1
            r -= 1
        while n > 0:
            print(4)
            nums1[r] = nums2[n-1]
            n -= 1
            r -= 1