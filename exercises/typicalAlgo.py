# Search one element in a list

def element_found_sequential_unordered(num, l_input):
    # First algo: sequential, unordered
    for element in l_input:
        if num == element:
            return True
    return False


def element_found_sequential_ordered(num, l_input):
    # Second algo: sequential, ordered
    l_internal = l_input # use of an internal list to avoid to modify the list outside the function
    l_input.sort()
    for element in l_internal:
        if num == element:
            return True
    return False

def element_found_binary_search(num, l_input):
    # Second algo: binary search


if __name__ == '__main__':
    l = [5, 9, 7, 13, 15, 1, 11]
    n = 13
    if element_found_sequential_ordered(n, l):
        print("found")
    else:
        print("not found")
