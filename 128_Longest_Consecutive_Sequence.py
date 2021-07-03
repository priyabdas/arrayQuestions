# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

def longestConsecutiveElements(array):
    array = set(array)
    #print(array)
    best =0
    for i in array:
        if i-1 not in array:
            y = i + 1
            while y in array:
                y += 1
            best = max(best,y - i)

    return best


def main():
    array = [100,4,200,1,3,2]
    print(longestConsecutiveElements(array))


if __name__ == "__main__":
    main()
