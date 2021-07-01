# Given two non empty arrays find if the 2nd array
# is a valid sequence of 1st one
# Ex Array1 = [5, 1, 22, 25 , 6 , -1 , 8 , 10 ]
#    array2 = [1 , 6, -1 , 10]
#    result is true


def isValidSubsequence(array, sequence):
	idx = 0
	idy = 0
	while idx < len(array) and idy < len(sequence):
		
		if array[idx] == sequence[idy]:
			idy = idy+1

		idx = idx+1
	return idy == len(sequence)


def main():
    arr = [5, 1, 22, 25 , 6 , -1 , 8 , 10]
    seq = [1 , 6, -1 , 10]
    targetSum = 34
    res = isValidSubsequence(arr, seq)
    print (res)


if __name__ == "__main__":
    main()
