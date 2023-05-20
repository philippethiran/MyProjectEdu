# Search one element in a list

def element_found_sequential_unordered(num, l_input):
    # First algo: sequential, unordered
    for element in l_input:
        if num == element:
            return True
    return False


def element_found_sequential_ordered(num, l_input):
    # Second algo: sequential, ordered
    l_internal = l_input.copy()   # use of an internal list to avoid to modify the list outside the function
    l_internal.sort()
    for element in l_internal:
        if num == element:
            return True
    return False


def element_found_binary_search(target,  l_input, low, high):
    # Second algo: binary search - recursive approach: see here for more info: https://en.wikipedia.org/wiki/Binary_search_algorithm
    # Return the position of the found element; -1 if not found
    if high >= 1:
        mid = (low + high) // 2  # integer division
        if target == l_input[mid]:  # Base condition (target value is found)
            return mid
        elif target < l_input[mid]:  # discard all elements in the right search space, including the middle element
            return element_found_binary_search(target, l_input, low, mid - 1)
        else:
            return element_found_binary_search(target, l_input, mid + 1, high)
    else:
        return -1


def fact(n):
    # Classical example of factorial
    if n == 0:
        return 1  # Base case
    return (n * fact(n - 1))  # Not a tail-recursive call


if __name__ == '__main__':

    # Find an element in a list:
    l = [5, 9, 7, 13, 15, 1, 11]
    n = 6
    if element_found_sequential_ordered(n, l):
        print("found")
    else:
        print("not found")

    # Some recursive functions
    print (l)
    print(element_found_binary_search(n, l, 0 ,len(l)-1))

    print(fact(5))
