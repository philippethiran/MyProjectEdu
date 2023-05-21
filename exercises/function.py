

# The two following functions show how to pass by reference or value in Python

def function_value(input):
    # simple function for showing the pass-by-value
    # input is immutable
    input += 100
    print("Inside function call ", input)


def function_ref(input2):
    # simple function for showing the reference
    # input2 is a list -> mutable
    input2.append('B')
    print("Inside function call", input2)


if __name__ == '__main__':
    # showing the pass-by-value
    input = 100
    print("Before function call ", input)
    function_value(input)
    print("After function call ", input)

    # showing the pass-by-reference
    input2 = ['A']
    print("Before function call ", input2)
    function_ref(input2)
    print("After function call ",input2)