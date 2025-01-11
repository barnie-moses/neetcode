class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        max_h = height[l]
        max_arr = [0] * len(height)
        while l < len(height):
            max_h = max(max_h, height[l])
            max_arr[l] = max_h
            l +=1
       
        r = len(height)-1
        rmax_h = height[r]
        rmax_arr = [0] * len(height)
        while r >= 0:
            rmax_h = max(rmax_h, height[r])
            rmax_arr[r] = rmax_h
            r -=1
    
        trapped_water = 0
        for i in range(len(height)):
            h = min(max_arr[i], rmax_arr[i])
            if h - height[i] >=0:
                trapped_water += h - height[i]
        return trapped_water