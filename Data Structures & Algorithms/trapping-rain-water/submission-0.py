class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        water = 0
        leftMax, rightMax = height[left], height[right]

        while left < right:  

            # print(f'leftMax = {leftMax}, rightMax = {rightMax}')

            if leftMax < rightMax:
                water += max(0, min(leftMax, rightMax) - height[left])
                # print(f'Water = {water}')
                left += 1
                leftMax = max(leftMax, height[left])

            elif leftMax > rightMax:
                water += max(0, min(leftMax, rightMax) - height[right])
                # print(f'Water = {water}')
                right -= 1
                rightMax = max(rightMax, height[right])

            else:
                water += max(0, min(leftMax, rightMax) - height[left])
                # print(f'Water = {water}')
                left += 1
                leftMax = max(leftMax, height[left])

        return water

        