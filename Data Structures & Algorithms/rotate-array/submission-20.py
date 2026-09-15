class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = start = 0

        while count < n:
            curr_i = start
            prev_val = nums[curr_i]

            while True:
                next_i = (curr_i + k) % n
                nums[next_i], prev_val = prev_val, nums[next_i]
                curr_i = next_i
                count += 1

                if curr_i == start:
                    break
            start += 1