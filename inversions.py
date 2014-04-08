def mahonian_row(n):
    '''Generates coefficients in expansion of 
    Product_{i=0..n-1} (1+x+...+x^i)
    **Requires that n is a positive integer'''
    # Allocate space for resulting list of coefficients?
    # Initialize them all to zero?
    #max_zero_holder = [0] * int(1 + (n * 0.5) * (n - 1))

    # Current max power of x i.e. x^0, x^0 + x^1, x^0 + x^1 + x^2, etc.
    # i + 1 is current row number we are computing
    i = 1
    # Preallocate result
    # Initialize to answer for n = 1
    result = [1]
    while i < n:
        # Copy previous row of n into prev
        prev = result[:]
        # Get space to hold (i+1)st row
        result = [0] * int(1 + ((i + 1) * 0.5) * (i))
        # Initialize multiplier for this row
        m = [1] * (i + 1)
        # Multiply
        for j in range(len(m)):
            for k in range(len(prev)):
                result[k+j] += m[j] * prev[k]
        # Result now equals mahonian_row(i+1)
        # Possibly should be memoized?
        i = i + 1
    return result


def main():
    t = int(raw_input())
    for _ in xrange(t):
        n, k = (int(s) for s in raw_input().split())
        row = mahonian_row(n)
        if k < 0 or k > len(row) - 1:
            print 0
        else:
            print row[k]


if __name__ == '__main__':
    main()
