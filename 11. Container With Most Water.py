height = [1,8,6,2,5,4,8,3,7]
def maxArea(height):
        """ The code starts here."""
        max_area = 0
        start_pointer = 0
        last_pointer = len(height) - 1
        while start_pointer < last_pointer:
            if height[last_pointer] < height[start_pointer]:
                max_area = max(max_area, (last_pointer - start_pointer) * height[last_pointer])
                last_pointer -= 1
            else:
                max_area = max(max_area, (last_pointer - start_pointer) * height[start_pointer])
                start_pointer += 1
        return max_area
        """ The code ends here."""
print(maxArea(height))