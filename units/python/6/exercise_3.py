
def parse_line(equation):
    """
    Parses the given equation of line in y = mx + c, and returns
    the values of m and c.
    """

    # Split the equation with '=' into LHS and RHS.
    rhs = equation.split('=')[1]

    # Split the RHS into two parts 'mx' and 'c' with '+' operator.
    parts = rhs.split('+')

    # Get the value of 'm' from the first part, 'mx'.
    m = parts[0].replace('x', '').strip()

    # Get the value of 'c' from the second part.
    c = parts[1].strip()

    return (float(m), float(c))


def main():
    """
    The main function that actually executes the program.
    """
    
    print('Enter equations of lines in y = mx + c form:')

    # Get the equations of two lines from the user.
    equation1 = input('Line 1: ')
    equation2 = input('Line 2: ')

    line1 = parse_line(equation1)
    line2 = parse_line(equation2)

    print('Line 1: ', line1)
    print('Line 2: ', line2)


# Run the program
main()
