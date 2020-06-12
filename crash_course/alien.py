'''Playing with dictionaries'''
# Default:ALIEN_COLOR = 'green'

# Default:
# Default:if 'red' in ALIEN_COLOR:
# Default:print("You missed the alien, you get no points")
# Default:elif 'yellow' in ALIEN_COLOR:
# Default:print("You wounded but didn't kill the alien, you get 1 point")
# Default:else:
# Default:if 'green' in ALIEN_COLOR:
# Default:print("Good work, the alien is dead, you get 5 points")

# Default:
alien_0 = {'color': 'green', 'points': 5}

# Default:
print(alien_0)
# Default:print(alien_0['points'])
del alien_0['points']
print(alien_0)
# Default:
# Default:NEW_POINTS = alien_0['points']
# Default:print(f"You just earned {NEW_POINTS} points!")

# Default:
# Default:alien_0['x_position'] = 0
# Default:alien_0['y_position'] = 25
# Default:print(alien_0)

# Default:
# Default:alien_0 = {}
# Default:alien_0['color'] = 'yellow'
# Default:alien_0['points'] = 10

# Default:alien_0 = {'color': 'green'}
# Default:print(f"The alien is {alien_0['color']}.")
# Default:alien_0['color'] = 'yellow'
# Default:print(f"The alien is now {alien_0['color']}.")
# Default:alien_0['color'] = 'red'

# Default:alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# Default:print(f"Original position: {alien_0['x_position']}")

# Default:
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
# new speed!
# Default:alien_0['speed'] = 'fast'

# Default:
# Default:if alien_0['speed'] == 'slow':
# Default:X_INCREMENT = 1
# Default:elif alien_0['speed'] == 'medium':
# Default:X_INCREMENT = 2
# Default:else:
# This must be a fast alien.
# Default:X_INCREMENT = 3

# Default:
# The new position is the old position plus the increment.
# Default:alien_0['x_position'] = alien_0['x_position'] + X_INCREMENT

# Default:
