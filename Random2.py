import random
import sys

#List of characters
Characters = [	"Amber", 	"Barbara", 	"Bennet", 	"Candace", 	"Collei",
				"Diluc", 	"Diona", 	"Dori", 	"Eula",		"Fischl",
				"Ganyu",	"Jean", 	"Kazuha",	"Ayaka",	"Keqing",
				"Lisa",		"Mona",		"Noelle",	"Raiden",	"Rosaria",
				"Kokomi",	"Sayu",		"Sucrose",	"Xiangling",	"Xingqiu",
				"Yanfei",	"Yun Jin"
				]


numberOfChars = int(sys.argv[1])
fileName = 'genshinWeights.txt'

"""
selectedChars = random.sample(Characters, k = numberOfChars)

print("Characters are: \n")
for c in selectedChars:
	#print(c, end = " ")
	print(c , "\n")
"""

#Read in stuff from file
with open(fileName,'r') as file:
	fileContents = file.read().splitlines()

#Create dictionary
characterDictionary = dict()
selectedChars = []

i = 0
while i < len(fileContents):
	characterDictionary[fileContents[i]] = int(fileContents[i+1])
	i = i+2

#Print current characters and weight values
print("\n", characterDictionary, "\n")

#itirate over numberOfChars
#generate random character
#add it to the list of selected chracters
#remove it from the dictionary to avoid repeats
for n in range(numberOfChars):
	randChar = random.choices(list(characterDictionary.keys()), weights = list(characterDictionary.values()))
	selectedChars.append(randChar[0])
	characterDictionary.pop(randChar[0])

#up the weight of non selected characters in the dictionary
for key in characterDictionary:
	characterDictionary[key] = characterDictionary.get(key) + 1

#add selected characters back to dictionary with a weight reset to 1
for selChar in selectedChars:
	characterDictionary[selChar] = 1

#rewrite the new dictionary to the file
with open(fileName, 'w') as file:
	for key in characterDictionary:
		file.write(key + '\n')
		file.write(str(characterDictionary[key]) + '\n')


print("Characters are: \n")
for c in selectedChars:
	#print(c, end = " ")
	print(c , "\n")

#print(selectedChars)
#print(characterDictionary)