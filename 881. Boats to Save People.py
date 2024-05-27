people = [3,2,2,1]
limit = 3
def numRescueBoats(people, limit):
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
print(numRescueBoats(people, limit))