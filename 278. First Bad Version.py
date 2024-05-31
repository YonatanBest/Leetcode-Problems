n = 5
def firstBadVersion(n):
        """ The code starts here."""
        min_f = 1
        max_f = n
        f = 1
        while min_f <= max_f:
            mid_f = (min_f + max_f) // 2
            if isBadVersion(mid_f): #This function is given by (handed by) the leetcode itself, so don't worry about it.
                f = mid_f
                max_f = mid_f - 1
            else:
                min_f = mid_f + 1
                
        return f
        """ The code ends here."""
print(firstBadVersion(n))