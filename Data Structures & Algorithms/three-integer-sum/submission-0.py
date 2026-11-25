class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        seen = set()
        result = []


        i = 0
        while i< len(nums) -2:

            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1

                elif total < 0:
                    left += 1

                elif total == 0:
                    triplet = tuple([nums[i],nums[left],nums[right]])

                    if triplet not in seen:
                        seen.add(triplet)
                        result.append(list(triplet))
                        print(result)
                    right -= 1
                    left += 1
            
            i += 1
        

        return result

        