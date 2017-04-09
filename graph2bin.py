import math

file = open("graph.txt", "r")
fileContents = file.read()
file.close()
fileContents = ''.join(fileContents.split())
nums = []
#print len(fileContents)
numNodes = len(fileContents)/2
k = int(math.ceil(math.log(numNodes, 2)))

for num in range(len(fileContents)):
	nums.append(bin(int(fileContents[num]))[2:].zfill(k))
file = open("translate.txt", "w")
for num in range(len(nums)):
	file.write(nums[num])
	file.write(" ")
file.close()

print("finished translating")