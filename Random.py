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

selectedChars = random.sample(Characters, k = numberOfChars)

print("Characters are: \n")
for c in selectedChars:
	#print(c, end = " ")
	print(c , "\n")

