class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area, left, right = 0, 0, len(heights)-1

        while left < right :

            curr_area = min(heights[left], heights[right]) * (right - left)

            if area < curr_area:
                area = curr_area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return area
        