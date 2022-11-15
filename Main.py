
import math

def integerToRoman(A):
	romansDict = \
		{
			1: "I",
			5: "V",
			10: "X",
			50: "L",
			100: "C",
			500: "D",
			1000: "M",
			5000: "G",
			10000: "H"
		}

	div = 1
	while A >= div:
		div *= 10

	div /= 10

	ref = ""

	while A:

		# main significant digit extracted
		# into lastNum
		lastNum = int(A / div)

		if lastNum <= 3:
			ref += (romansDict[div] * lastNum)
		elif lastNum == 4:
			ref += (romansDict[div] +
						romansDict[div * 5])
		elif 5 <= lastNum <= 8:
			ref += (romansDict[div * 5] +
			(romansDict[div] * (lastNum - 5)))
		elif lastNum == 9:
			ref += (romansDict[div] +
						romansDict[div * 10])

		A = math.floor(A % div)
		div /= 10
		
	return ref
x = int(input("Enter A Number To Convert it To Roamn Number : "))
print("Roman value for the integer is:"
				+ str(integerToRoman(x)))
