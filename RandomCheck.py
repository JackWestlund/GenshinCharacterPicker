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

CharacterPickCount = {'Amber': 0, 'Barabara': 0, 'Bennet': 0, 'Candace': 0, 'Collei': 0,
						'Diluc': 0, 'Diona': 0, 'Dori': 0, 'Eula': 0, 'Fischl': 0,
						'Ganyu': 0, 'Jean': 0, 'Kazuha': 0, 'Ayaka': 0, 'Keqing': 0,
						'Lisa': 0, 'Mona': 0, 'Noelle': 0, 'Radien': 0, 'Rosaria': 0,
						'Kokomi': 0, 'Sayu': 0, 'Sucrose': 0, 'Xiangling': 0, 'Xingqiu': 0,
						'Yanfei': 0, 'Yun Jin': 0}

characterDictionary = {'Amber': 1, 'Barabara': 1, 'Bennet': 1, 'Candace': 1, 'Collei': 1,
						'Diluc': 1, 'Diona': 1, 'Dori': 1, 'Eula': 1, 'Fischl': 1,
						'Ganyu': 1, 'Jean': 1, 'Kazuha': 1, 'Ayaka': 1, 'Keqing': 1,
						'Lisa': 1, 'Mona': 1, 'Noelle': 1, 'Radien': 1, 'Rosaria': 1,
						'Kokomi': 1, 'Sayu': 1, 'Sucrose': 1, 'Xiangling': 1, 'Xingqiu': 1,
						'Yanfei': 1, 'Yun Jin': 1}

#numberOfChars = int(sys.argv[1])

"""
selectedChars = random.sample(Characters, k = numberOfChars)

print("Characters are: \n")
for c in selectedChars:
	#print(c, end = " ")
	print(c , "\n")
"""

"""
#Read in stuff from file
with open('genshinWeights.txt','r') as file:
	fileContents = file.read().splitlines()

#Create dictionary
#characterDictionary = dict()


i = 0
while i < len(fileContents):
	characterDictionary[fileContents[i]] = int(fileContents[i+1])
	i = i+2
"""

for i in range(100000):

	selectedChars = []

	#itirate over numberOfChars
	#generate random character
	#add it to the list of selected chracters
	#remove it from the dictionary to avoid repeats
	for n in range(2):
		randChar = random.choices(list(characterDictionary.keys()), weights = list(characterDictionary.values()))
		selectedChars.append(randChar[0])
		characterDictionary.pop(randChar[0])

	#up the weight of non selected characters in the dictionary
	for key in characterDictionary:
		characterDictionary[key] = characterDictionary.get(key) + 1

	#add selected characters back to dictionary with a weight reset to 1
	for selChar in selectedChars:
		characterDictionary[selChar] = 1
		
		CharacterPickCount[selChar] += 1
"""
#rewrite the new dictionary to the file
with open('genshinWeights.txt', 'w') as file:
	for key in characterDictionary:
		file.write(key + '\n')
		file.write(str(characterDictionary[key]) + '\n')
"""





"""
print("Characters are: \n")
for c in selectedChars:
	#print(c, end = " ")
	print(c , "\n")
"""
#print(selectedChars)
#print(characterDictionary)

print(CharacterPickCount)