import os
import sys
from decimal import Decimal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt	
import numpy as np

beginningPlace = os.getcwd()
destiny = sys.argv[1:]


for items in destiny:
	changePlace = beginningPlace + "/" + items
	os.chdir(changePlace)
	for itemInSub in os.listdir(changePlace):
		if itemInSub.endswith('.txt'):
			verticalName = []
			horizontalName = []
			file = open(itemInSub,"r")
			readAll = file.read()
			x = readAll.split()
			for charac in x:
				if charac not in verticalName:
					if charac.isalpha() == True:
						verticalName.append(charac)
						horizontalName.append(1)
				else:
					position = verticalName.index(charac)
					horizontalName[position] = horizontalName[position] + 1
			timeOfGraph = len(verticalName) / 150
			totalSum = 0.0
			for i in range(len(horizontalName)):
				totalSum = horizontalName[i] + totalSum

			for x in range(len(horizontalName)):
				horizontalName[x] = float(horizontalName[x] / totalSum)
					
			if timeOfGraph == 0:
				tuple(verticalName)
				plt.figure(figsize=(10,20))
				y_pos = np.arange(len(verticalName))
				cutLength = len(itemInSub) - 3
				nameForTitle = itemInSub[:cutLength - 1]+"_hist"
				graphTitle = nameForTitle + " Word Count Distribution"
				plt.title(graphTitle)
				plt.ylabel("Words")
				plt.xlabel("Distribution")
				plt.barh(y_pos,horizontalName,align='center', alpha=0.5,height=0.5)
				plt.yticks(y_pos, verticalName)
				name =  itemInSub[:cutLength-1]+"_hist"+".png" 
				plt.savefig(name)
				plt.clf()
				file.close()
			else:
				addHun = 0
				for i in range(timeOfGraph + 1):
					if (len(verticalName) - addHun) <= 150:
						ans = tuple(verticalName[addHun:])
						plt.figure(figsize=(10,25))
						y_pos = np.arange(len(ans))
						cutLength = len(itemInSub) - 3
						nameForTitle = itemInSub[:cutLength - 1]+"_hist"+str(i)
						graphTitle = nameForTitle + " Word Count Distribution"
						plt.title(graphTitle)
						plt.ylabel("Words")
						plt.xlabel("Distribution")
						plt.barh(y_pos,horizontalName[addHun:],align='center')
						plt.yticks(y_pos, ans)
						name =  itemInSub[:cutLength - 1]+"_hist"+str(i)+".png" 
						addHun = addHun + 150
						plt.savefig(name)
						plt.clf()
						ans = tuple(verticalName[addHun:addHun + 150])
						break

					ans = tuple(verticalName[addHun:addHun + 150])
					cutLength = len(itemInSub) - 3
					name =  itemInSub[:cutLength - 1]+"_hist"+str(i)+".png"
					nameForTitle = itemInSub[:cutLength - 1]+"_hist"+str(i)
					plt.figure(figsize=(10,25))
					y_pos = np.arange(len(ans))
					graphTitle = nameForTitle + " Word Count Distribution"
					plt.title(graphTitle)
					plt.ylabel("Words")
					plt.xlabel("Distribution")
					plt.barh(y_pos,horizontalName[addHun:addHun + 150],align='center')
					plt.yticks(y_pos, ans)
					addHun = addHun + 150
					plt.savefig(name)
					plt.clf()

	os.chdir(beginningPlace)