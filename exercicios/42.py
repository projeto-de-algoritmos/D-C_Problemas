class Solution:
    def trap(self, height: List[int]) -> int:

        def calculate_pool(s):
            h = min(max(height[0:s+1]), max(height[s:]))

            if h == height[s]:
                return 0, s, s

            l = s
            while l >= 0 and height[l] < h:
                l -= 1

            r = s
            while r < len(height) and height[r] < h:
                r += 1

            volume = 0
            for i in range(l + 1, r):
                volume += h - height[i]
            
            return volume, l, r

        if len(height) <= 2:
            return 0

        volume, l, r = calculate_pool(len(height) // 2)

        return volume + self.trap(height[0:l+1]) + self.trap(height[r:])