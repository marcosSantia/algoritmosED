
# Create two stacks for characters from episode V and episode VII
stack_episode_v = []
stack_episode_vii = []

# Populate the stacks with characters from each episode
# ...

# Create a new stack to store the intersection of characters
stack_intersection = []

# Iterate over the characters in stack_episode_v
while stack_episode_v:
    character = stack_episode_v.pop()
    
    # Check if the character is also in stack_episode_vii
    if character in stack_episode_vii:
        stack_intersection.append(character)

# Print the characters that appear in both episodes
print("Characters that appear in both episodes:")
while stack_intersection:
    print(stack_intersection.pop())