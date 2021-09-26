# Write a function that takes this data as input and returns two collections: one containing all individuals with
# zero known parents, and one containing all individuals with exactly one known parent.
#
# Output may be in any order:
#
# find_nodes_with_zero_and_one_parents(parent_child_pairs) => [
# [1, 2, 4, 15], # Individuals with zero parents
# [5, 7, 8, 11] # Individuals with exactly one parent
# ]
#
# n: number of pairs in the input
#
# '''
#
# parent_child_pairs = [
# (1, 3), (2, 3), (3, 6), (5, 6), (15, 9),
# (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
# ]


parent_child_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (15, 9), (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)]


def get_adjacency_list():
    child_parent_map = {}
    for parent, child in parent_child_pairs:

        if child not in child_parent_map:
            child_parent_map[child] = []
            child_parent_map[child].append(parent)
        else:
            child_parent_map[child].append(parent)

        if parent not in child_parent_map:
            child_parent_map[parent] = []

    return child_parent_map


def zero_known_parents_and_exactly_one_parent():
    child_parent_map = get_adjacency_list()
    zero_parents = []
    one_parent = []
    for child in child_parent_map:
        if len(child_parent_map[child]) == 0:
            zero_parents.append(child)
        elif len(child_parent_map[child]) == 1:
            one_parent.append(child)
    print(zero_parents)
    print(one_parent)


zero_known_parents_and_exactly_one_parent()
