people = [3,2,2,1]
limit = 3
def numRescueBoats(people, limit):
    """ The code starts here."""
    boats = 0
    people.sort()
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            boats += 1
            i += 1
            j -= 1
        else:
            boats += 1
            j -= 1
    return boats
    """ The code ends here."""
print(numRescueBoats(people, limit))