#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	arg = sys.argv
	sum = 0
	for i in range(len(arg)):
		sum += int(arg[i])
	print(sum)	
