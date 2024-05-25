
s = "III"
def romanToInt(s: str) -> int:
        """ The code starts here."""
        I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
        num = 0
        arr=[]
        for i in s:
            arr.append(i)
        for i in range(0, len(arr)):
            if arr[i] == "M":
                num += 1000
            elif arr[i] == "D":
                num += 500
            elif arr[i] == "C":
                if len(arr) - 1 == i:
                    num += 100
                else:
                    if arr[i+1] == "D" or arr[i+1] == "M":
                        num -= 100
                    else:
                        num +=100
            elif arr[i] == "L":
                num += 50
            elif arr[i] == "X":
                if len(arr) - 1 == i:
                    num += 10
                else:
                    if arr[i+1] == "L" or arr[i+1] == "C":
                        num -= 10
                    else:
                        num +=10
            elif arr[i] == "V":
                num += 5
            elif arr[i] == "I":
                if len(arr) - 1 == i:
                    num += 1
                else:
                    if arr[i+1] == "V" or arr[i+1] == "X":
                        num -= 1
                    else:
                        num +=1
        return num
        """ The code ends here."""
print(romanToInt(s))