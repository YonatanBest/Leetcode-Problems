s = "abc"
def clearDigits(s):
        """ The code starts here."""
        arr = []*len(s)
        for i in s:
            arr.append(i)
        a = 0
        s = len(arr)
        while a < s:
            if arr[a].isdigit():
                arr.pop(a)
                arr.pop(a- 1)
                s = len(arr)
                a = 0
                continue
            a += 1
        ans = ""
        for x in arr:
            ans = ans + x
        return ans
        """ The code ends here."""
print(clearDigits(s))