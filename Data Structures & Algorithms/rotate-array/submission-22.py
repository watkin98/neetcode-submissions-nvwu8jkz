class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        start = count = 0

        while count < n:
            curr_i = start
            prev = nums[curr_i]
            do_once = True

            while do_once or curr_i != start:
                do_once = False

                next_i = (curr_i + k) % n
                nums[next_i], prev = prev, nums[next_i]
                curr_i = next_i
                count += 1
                
            start += 1