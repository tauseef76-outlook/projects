# Given an array A of n positive numbers.
# The task is to find the first Equilibium Point
# in the array. Equilibrium Point in an array is
# a position such that the sum of elements before
# it is equal to the sum of elements after it.

import math


class Solution:
    # Complete this function

    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        # Your code here
        if (N == 1):
            return 1
        larr = 0
        rarr = sum(A) - A[0]

        for i in range(0, N-1):
            if(larr == rarr):
                return i+1

            larr += A[i]
            rarr -= A[i+1]

        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():

    N = 5

    A = [1, 3, 5, 2, 2]
    ob = Solution()

    print(ob.equilibriumPoint(A, N))


if __name__ == "__main__":
    main()
