heights = [1,1,4,2,1,3]
def heightChecker(heights):
        """ The code starts here."""
        heightsort = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heightsort[i] != heights[i]:
                count += 1
        return count
        """ The code ends here."""
print(heightChecker(heights))