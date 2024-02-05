#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	arg = sys.argv
	_sum = 0
	for i in range(1, len(arg)):
		_sum += int(arg[i])
	print(_sum)	
