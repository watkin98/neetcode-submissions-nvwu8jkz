class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        i = 0
        while True:
            if nums[slow] == nums[fast] and slow != fast:
                return nums[slow]

            slow = slow + 1 if slow < (len(nums) - 1) else 0
            #print(slow)
            fast = fast + 2 if fast < (len(nums) - 2) else 0
            # i += 1

            # if i > 10:
            #     break
