def maxArea(height) -> int:
        max = 1
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                print(min(height[i], height[j]), '*', (j-i), '=', min(height[i], height[j]) * (j-i))
                if (min(height[i], height[j]) * (j-i)) > max:
                    max = min(height[i], height[j]) * (j-i)
        return max
#correct solution but we have a time limit exceeded when a large size list is given