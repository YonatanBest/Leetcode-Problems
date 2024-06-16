plants = [2,2,3,3]
capacity = 5
def wateringPlants(plants, capacity):
        """ The code starts here."""
        step = 1
        cap = capacity
        for i in range(1, len(plants)):
            cap -= plants[i-1]
            step += 1
            if cap < plants[i]:
                step += 2*(i)
                cap = capacity
        return step
        """ The code ends here."""
print(wateringPlants(plants, capacity))