def people_not_following_you_back_(followers, following):

    """Compares two lists and highlights names not in list one."""
    names_not_in_list_one = [name for name in followers if name not in following]
    return names_not_in_list_one

# Example usage:
followers = ["Alice", "Bob", "Charlie", "David"]
following = ["Charlie", "David", "Eve", "Frank"]
highlighted_names = highlight_names_not_in_list_one(followers, following)
print("Names not in list one:", highlighted_names)

