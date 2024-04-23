def people_not_following_you_back(followers, following):

    # Compares the two lists and highlights names not in follower list 

    names_followers = [name for name in following if name not in followers]
    return names_followers

# Example usage:
followers = ["Alice", "Bob", "Charlie", "David"]
following = ["Charlie", "David", "Eve", "Frank"]
highlighted_names = people_not_following_you_back(followers, following)
print("Names not following you back:", highlighted_names)


