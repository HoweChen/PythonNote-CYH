from typing import List, Tuple


def enlarge_list(input_list: List[List[int]]) -> List:
    original_length = len(input_list)
    new_length = original_length + 2
    row_border = ["inf"] * new_length
    extended_list = [row_border]

    new_map = [row_border]
    for row in input_list:
        # print(row)
        # print(["inf"] + row + ["inf"])
        extended_list.append(["inf"] + row + ["inf"])
    extended_list.append(row_border)
    return extended_list

def is_sink(m: List[List[int]], c: List[int]) -> bool:
    """
    Returns True if and only if c is a sink in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> is_sink(m, [0,0])
    True
    >>> is_sink(m, [2,2])
    True
    >>> is_sink(m, [3,0])
    False
    >>> m = [[1,2,3],
             [2,1,3],
             [5,4,3]]
    >>> is_sink(m, [1,1])
    True
    """
    #Your code goes here
    if c[0] > len(m) - 1 or c[1] > len(m) - 1:
        return False
    else:
        new_list = enlarge_list(m)
        for index in range(len(c)):
            c[index] += 1

        local_minimum = new_list[c[0]][c[1]]
        for i in range(-1, 2):
            for j in range(-1, 2):
                target_num = new_list[c[0] + i][c[1] + j]
                if target_num == "inf":
                    continue
                elif target_num < local_minimum:
                    return False
        return True


def find_sink_point(m: List[List[int]], c: List[int]) -> Tuple[int, int]:
    # note that m stands for the extended_list
    new_list = enlarge_list(m)

    local_minimum = new_list[c[0]][c[1]]
    for i in range(-1, 2):
        for j in range(-1, 2):
            target_num = new_list[c[0] + i][c[1] + j]
            if target_num == "inf":
                continue
            elif target_num < local_minimum:
                local_minimum = target_num
    for i in range(-1, 2):
        for j in range(-1, 2):
            if new_list[c[0] + i][c[1] + j] == local_minimum:
                return c[0] + i, c[1] + j


def find_local_sink(m: List[List[int]], start: List[int]) -> List[int]:
    """
    Given a non-empty elevation map, m, starting at start,
    will return a local sink in m by following the path of lowest
    adjacent elevation.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]]
    >>> find_local_sink(m, [0,0])
    [3,3]
    >>> m = [[ 5,70,71,80],
             [50, 4, 5,90],
             [60, 3,35, 2],
             [ 1,72, 6, 3]]
    >>> find_local_sink(m, [0,3])
    [2,3]
    >>> m = [[9,2,3],
             [6,1,7],
             [5,4,8]]
    >>> find_local_sink(m, [1,1])
    [1,1]
    """
    # Your code goes here
    start[0] += 1
    start[1] += 1
    new_x, new_y = find_sink_point(m, start)
    while start != [new_x, new_y]:
        return find_local_sink(m, [new_x - 1, new_y - 1])
    return [new_x - 1, new_y - 1]





def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    """
    Given an elevation map m, a start cell s, a destination cell d, and
    the an amount of supplies returns True if and only if a hiker could reach
    d from s using the strategy dscribed in the assignment .pdf. Read the .pdf
    carefully. Assume d is always south, east, or south-east of s. The hiker
    never travels, north, west, nor backtracks.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,4,3],
             [2,3,5],
             [5,4,3]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    True
    >>> can_hike_to(m, [0,0], [0,0], 0)
    True
    >>> can_hike_to(m, [0,0], [2,2], 3)
    False
    >>> m = [[1,  1,100],
             [1,100,100],
             [1,  1,  1]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    False
    >>> can_hike_to(m, [0,0], [2,2], 202)
    True
    """
    # Your code goes here

    if s[0] > d[0] or s[1] > d[1]:
        return False
    elif supplies <= 0 and s != d:
        return False
    elif s == d and supplies >= 0:
        return True
    else:
        base = m[s[0]][s[1]]
        try:
            east_val = m[s[0]][s[1] + 1]
        except IndexError:
            east_val = None
        try:
            south_val = m[s[0] + 1][s[1]]
        except IndexError:
            south_val = None
        east_difference = abs(east_val - base) if east_val else None
        south_difference = abs(south_val - base) if south_val else None
        if east_difference is not None and south_difference is not None:
            go_east = east_difference <= south_difference
        elif east_difference and not south_difference:
            go_east = True
        else:
            go_east = False
        if go_east:
            supplies = supplies - east_difference
            s[1] += 1
        else:
            supplies = supplies - south_difference
            s[0] += 1
        return can_hike_to(m, s, d, supplies)



# testing part

m = [[5, 70, 71, 80], [50, 4, 30, 90], [60, 3, 35, 95], [10, 72, 2, 1]]
m2 = [[5, 70, 71, 80], [50, 4, 5, 90], [60, 3, 35, 2], [1, 72, 6, 3]]
m3 = [[9, 2, 3], [6, 1, 7], [5, 4, 8]]
m4 = [[5, 70, 71, 80], [50, 4, 5, 90], [60, 3, 35, 2], [1, 72, 6, 3]]

m_sol = [3, 3]
m2_sol = [2, 3]
m3_sol = [1, 1]
m4_sol = [2, 3]

m5 = [[1, 4, 3], [2, 3, 5], [5, 4, 3]]
m6 = [[1, 1, 100], [1, 100, 100], [1, 1, 1]]

assert is_sink([[1, 2, 3], [2, 3, 3], [5, 4, 3]], [0, 0]) == True
assert is_sink([[1, 2, 3], [2, 3, 3], [5, 4, 3]], [2, 2]) == True
assert is_sink([[1, 2, 3], [2, 3, 3], [5, 4, 3]], [3, 0]) == False
assert is_sink([[1, 2, 3], [2, 1, 3], [5, 4, 3]], [1, 1]) == True

assert find_local_sink(m, [0, 0]) == m_sol
assert find_local_sink(m2, [0, 3]) == m2_sol
assert find_local_sink(m3, [1, 1]) == m3_sol
assert find_local_sink(m4, [0, 3]) == m4_sol

assert can_hike_to(m5, [0, 0], [2, 2], 4) == True
assert can_hike_to(m5, [0, 0], [0, 0], 0) == True
assert can_hike_to(m5, [0, 0], [2, 2], 3) == False
assert can_hike_to(m6, [0, 0], [2, 2], 4) == False
assert can_hike_to(m6, [0, 0], [2, 2], 202) == True
