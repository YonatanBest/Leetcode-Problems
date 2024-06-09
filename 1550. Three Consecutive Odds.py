arr = [2,6,4,1]
def threeConsecutiveOdds(arr):
        """ The code starts here."""
        for i in range(2, len(arr)):
            if arr[i - 2] % 2 and arr[i - 1] % 2 and arr[i] % 2:
                return True
        return False
        """ The code ends here."""
print(threeConsecutiveOdds(arr))