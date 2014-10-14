import sys

cycle = 1

def main():
	inputCount = 0
	count = 0
	lines = sys.stdin.readlines()
	for line in lines:
		if count == 0:
			inputCount = int(line)
		else:
			print(getUtopianNum(int(line)))

		count = count + int(line)

def getUtopianNum(n):
	global cycle
	cycle = 1
	h = 1
	while n > 0:
		h = getNewHeight(h)
		if cycle == 1:
			cycle = 2
		else:
			cycle = 1
		n = n - 1

	return h

def getNewHeight(h):
	global cycle
	if cycle == 1:
		return 2 * h
	else:
		return h + 1

main()

# print(getUtopianNum(4))