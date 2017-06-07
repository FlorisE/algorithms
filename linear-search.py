def linear_search(A, v):
    # at the start of each iteration of this loop
    # A[0..i] did not include the value
    for i, a in enumerate(A):
        if a == v:
            return i
    return None

A = [1, 2, 3, 4, 5]
print(linear_search(A, 5))
print(linear_search(A, 6))

# Initialization:
# A[0..i] is an empty list, hence it does not include the value
# Maintenance:
# If a value was found, the algorithm stops due to the return on line 10
# and hence the loop is not entered again
# Termination:
# If we never found the value in the list then we can conclude that the list
# does not contain the desired element
