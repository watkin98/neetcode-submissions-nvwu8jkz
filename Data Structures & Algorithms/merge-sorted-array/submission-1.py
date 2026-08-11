class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = 0, 0

        while ptr2 < len(nums2):
            if nums1[ptr1] == 0:
                nums1[ptr1] = nums2[ptr2]
                ptr2 += 1     
            elif nums2[ptr2] <= nums1[ptr1]:
                nums1.insert(ptr1, nums2[ptr2])
                nums1.pop()
                ptr2 += 1
                
            ptr1 += 1

            
            