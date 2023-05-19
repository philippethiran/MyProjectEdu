# Some typical examples of loops

def loop_while():
    count = 0
    while count < 10:
        count += 1
        if count == 5: break
        print("The value of the count is " + str(count))


def for_search_bad(item):
    # function to find whether a value is present or not in a sequence
    # bad as there is a condition of exiting the loop inside the body of the loop
    numbers = [5, 9, 10, 7, 13, 3, 20, 11]
    for val in numbers:
        if val == item:
            print("Item Found.")
            break
    else:
        print("Item Not Found!")


def for_search_good(item):
    # function to find whether a value is present or not in a sequence
    # good as all the conditions of loop exist are in the condition of the loop
    numbers = [5, 9, 10, 7, 13, 3, 20, 11]
    found = False
    pos = 0

    while (pos < len(numbers)-1) and (not found):
        if numbers[pos] == item:
            found = True
        pos += 1

    if found:
        print("Item Found!")
    else:
        print("Item Not Found!")


if __name__ == '__main__':
    loop_while()
    for_search_bad(19)
    for_search_good(9)
