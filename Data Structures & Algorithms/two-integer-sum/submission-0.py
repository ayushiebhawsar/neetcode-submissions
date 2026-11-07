class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref_dict = dict()

        for i in range(len(nums)):
            key = target - nums[i]
            # lst.append(i)
            if key not in ref_dict:
                ref_dict[key] = [i]
            else:
                ref_dict[key].append(i)

        for k in ref_dict:
            res = target - k 
            if res in ref_dict and k != res and ref_dict[k][0] != ref_dict[res][0]:
                return [ref_dict[k][0], ref_dict[res][0]]
            elif res in ref_dict and k == res and len(ref_dict[k]) >= 2 and ref_dict[k][0] != ref_dict[k][1]:
                return [ref_dict[k][0], ref_dict[k][1]]
        