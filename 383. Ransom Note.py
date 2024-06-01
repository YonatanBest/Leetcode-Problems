ransomNote = "a"
magazine = "b"
def canConstruct(ransomNote, magazine):
        """ The code starts here."""
        ranarr = []
        for k in ransomNote:
            ranarr.append(k)
        ranarr.sort()
        i = 0
        while i < len(ranarr):
            if not ranarr[i] in magazine:
                return False
            if ranarr.count(ranarr[i]) <= magazine.count(ranarr[i]):
                i += (ranarr.count(ranarr[i]))
            else:
                return False
        return True
        """ The code ends here."""
print(canConstruct(ransomNote, magazine))