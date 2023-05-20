# Here, you will find some interesting consequence of immutable or mutable types

# Compare search_element_1 and search_element_2 and search_element_3
# l_input is a list and used as a parameter of the function. As a list is immutable, this implicitly implies that
# the list is passed by reference! Hence, if you modify it within the function,
# the modification will be applied everywhere


def search_element_1(target, l_input):
    # l_input is passed by reference
    l_input.sort()
    for element in l_input:
        if target == element:
            return True
    return False


def search_element_2(target, l_input):
    # l_input will also be modified globally although we use an internal variable
    l_internal = l_input    # l_internal will refer to the same object id.
                            # Hence, when we modify l_internal, we also modify l_input
    l_internal.sort()
    for element in l_internal:
        if target == element:
            return True
    return False


def search_element_3(target, l_input):
    # l_input won't be modify as we copy it internally
    l_internal = l_input.copy()
    l_internal.sort()
    for element in l_internal:
        if target == element:
            return True
    return False
