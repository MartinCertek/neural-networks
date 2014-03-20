class Data:

	def getDataFromFile(self): 

		digits = []

		with open('p_data.txt', 'r') as dataFile:
      			for line in dataFile:
        		#poriesit spracovanie \n na konci v premennej out_bin
        			(inBin, outBin) = line.split('|') 
        			outBin = int(outBin)
        			inBin = eval(inBin)
        			digits.insert(len(digits),((inBin), outBin))  
        		#my_choices.insert(len(my_choices)+1, ((5,4),33))
        		#print inBin
        		#print outBin
		#print digits
		return digits

	def getData(self): 

		digits = []

		#musi byt dodrzana struktura oddelenia atributov pomocou "," a rozhodnutia pomocou "|"

		with open('p_data.txt', 'r') as dataFile:
      			for line in dataFile:
        		#poriesit spracovanie \n na konci v premennej out_bin
        			(inBin, outBin) = line.split('|') 
        			outBin = int(outBin)
        			inBin = eval(inBin)
        			digits.insert(len(digits),((inBin), outBin))  
        		#my_choices.insert(len(my_choices)+1, ((5,4),33))
        		#print inBin
        		#print outBin
		#print digits
		return digits