def count_arrangements(g, y, r, last_ball):
    # Base case: no balls left
    if g == 0 and y == 0 and r == 0:
        return 1
    
    count = 0
    # Try placing Green (0)
    if g > 0 and last_ball != 0:
        count += count_arrangements(g - 1, y, r, 0)
    # Try placing Yellow (1)
    if y > 0 and last_ball != 1:
        count += count_arrangements(g, y - 1, r, 1)
    # Try placing Red (2)
    if r > 0 and last_ball != 2:
        count += count_arrangements(g, y, r - 1, 2)
        
    return count

# For Input G=1, Y=1, R=1:
# We start with last_ball as -1 (none)
print(count_arrangements(4, 4, 4, 3)) # Output: 6