class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights)-1
        vol = 0
        while l < r:
            if heights[l] < heights[r]:
                h = heights[l]
                b = r-l
                l +=1
            else: 
                h = heights[r]
                b = r-l
                r -=1

            product = h * b
            vol = max(vol, product)
        
        return vol