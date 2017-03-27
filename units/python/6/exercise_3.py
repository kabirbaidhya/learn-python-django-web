
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


def intersection_point(line1, line2):
    """
    Calculates the intersection point of two lines given by their 
    parsed tuple containing slope & y-intercept. 
    """
    (m1, c1) = line1
    (m2, c2) = line2

    # Get the point of intersection
    x = (c1 - c2) / (m2 - m1)
    y = m1 * x + c1             # As we have y = mx + c

    return (x, y)


def main():
    """
    The main function that actually executes the program.
    """

    print('Enter equations of lines in y = mx + c form:\n')

    # Get the equations of two lines from the user.
    equation1 = input('Line 1: ')
    equation2 = input('Line 2: ')

    # Parse the two equations of two lines.
    line1 = parse_line(equation1)
    line2 = parse_line(equation2)

    # Print the intersection point.
    point = intersection_point(line1, line2)
    print('\nIntersection Point: (x, y) = ({}, {})'.format(*point))


# Run the program
main()
