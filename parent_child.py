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


# parent_child_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (15, 9), (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)]
parent_child_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),(4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)]

from collections import deque


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


# zero_known_parents_and_exactly_one_parent()

child1 = 6
child2 = 9
child3 = 3
child4 = 1


def do_bfs(child_parent_map, child):
    reacheable_parents_from_child = []
    queue = deque()
    queue.append(child)

    while queue:
        popped = queue.popleft()
        parents = child_parent_map[popped]
        for parent in parents:
            reacheable_parents_from_child.append(parent)
            queue.append(parent)

    return reacheable_parents_from_child


def has_any_common_ancestors():
    child_parent_map = get_adjacency_list()
    print(child_parent_map)
    child1_relations = do_bfs(child_parent_map, child1)
    child2_relations = do_bfs(child_parent_map, child2)

    child3_relations = do_bfs(child_parent_map, child3)
    child4_relations = do_bfs(child_parent_map, child4)

    print(child1_relations)
    print(child2_relations)
    print(child3_relations)
    print(child4_relations)

    temp = set(child1_relations)
    result = [parent for parent in child2_relations if parent in temp]

    temp1 = set(child3_relations)
    result1 = [parent for parent in child4_relations if parent in temp1]

    return len(result) > 0, len(result1) > 0


print(has_any_common_ancestors())
