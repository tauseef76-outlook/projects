# Given an array A of positive integers. Your task is to find the
# leaders in the array.
# An element of array is leader if it is greater than or
# equal to all the elements to its right side. The rightmost
# element is always a leader.


import math


class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, A, N):
        # Code here
        leader = []
        a = A[::-1]
        max = 0
        for items in a:
            if(max <= items):
                max = items
                leader.append(max)

        return (leader[::-1])


def main():

    N = 6

    A = [16, 17, 4, 3, 5, 2]
    obj = Solution()

    A = obj.leaders(A, N)

    for i in A:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
# } Driver Code Ends
