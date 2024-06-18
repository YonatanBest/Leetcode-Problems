ghosts = [[1,0],[0,3]]
target = [0,1]
def escapeGhosts(ghosts, target):
        """ The code starts here."""
        all = abs(target[0]) + abs(target[1])
        for i in ghosts:
            x = abs(i[0] - target[0])
            y = abs(i[1] - target[1])
            go = x + y
            if go <= all:
                return False
        return True
        """ The code ends here."""
print(escapeGhosts(ghosts, target))
