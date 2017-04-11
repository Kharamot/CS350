import math
import random
file = open("graph.txt", "w")
for i in range(0, 1024):
	file.write(str(i))
	file.write(" ")
	x = random.randint(0,1023)
	file.write(str(x))
	file.write("\n")

for i in range(0, 1024):
	x = random.randint(0,1023)
	file.write(str(x))
	file.write(" ")
	x = random.randint(0,1023)
	file.write(str(x))
	file.write("\n")
file.close()

file = open("graph.txt", "r")
fileContents = file.read()
file.close()
fileContents = fileContents.split()
print(fileContents)
nums = []
#print len(fileContents)
numNodes = len(fileContents)/2
k = int(math.ceil(math.log(1024, 2)))

for num in range(len(fileContents)):
	#print(num)
	nums.append(str(bin(int(fileContents[num]))[2:].zfill(k)))
file = open("translate.txt", "w")
for num in range(len(nums)):
	file.write(nums[num])
	file.write(" ")
file.close()

print("finished translating")