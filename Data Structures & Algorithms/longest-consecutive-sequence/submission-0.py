class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if num -1 not in nums_set:
                start_num = num
                curr_long = 1

                while start_num +1 in nums_set:
                    curr_long += 1
                    start_num += 1

                longest = max(longest, curr_long)
                
        return longest
        