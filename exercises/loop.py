# Some typical examples of loops

def loop_while():
    count = 0
    while count < 10:
        count += 1
        if count == 5: break
        print("The value of the count is " + str(count))


def for_search_bad(numbers, item):
    # function to find whether a value is present or not in a sequence
    # bad as there is a condition of exiting the loop inside the body of the loop
    for val in numbers:
        if val == item:
            print("Item Found.")
            break
    else:
        print("Item Not Found!")


def for_search_good(numbers, item):
    # function to find whether a value is present or not in a sequence
    # good as all the conditions of loop exist are in the condition of the loop
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


def for_search_even(numbers):
    # Python function using the break statement
    for i in numbers:
        # Come out of the loop if an even number is encountered.
        if i % 2 == 0:
            print("\nBreaking the Loop. Even Value Encountered.")
            break
        print(i, end=' ')


def for_search_even_good(numbers):
    # Python function not using the break statement
    found = False
    pos = 0

    while (pos < len(numbers)-1) and (not found):
        if numbers[pos] % 2 == 0:
            found = True
        pos += 1

    if found:
        print("\nEven Value Encountered.")





if __name__ == '__main__':
    numbersi = [5, 9, 7, 13, 15, 1, 11]
    loop_while()
    for_search_bad(numbersi, 19)
    for_search_good(numbersi, 9)
    for_search_even(numbersi)
    for_search_even_good(numbersi)