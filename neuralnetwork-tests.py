#from unittest import *
from neuralnetwork import *
from data import * 
from ast import literal_eval
import sys

def xorRun(learningRate, momentum, maxIterations, inN, hN):

   n_num = int(inN)
   h_num = int(hN)
   network = Network()
   inputNodes = [InputNode(i) for i in range(int(n_num))]
   hiddenNodes = [Node() for i in range(int(h_num))]
   outputNode = Node()

   # vytvori hrany medzi vstupnou vrstvou a skrytou vrstvou, vahy su random 
   i = 0
   for inputNode in inputNodes:
      i += 1
      j = 0
      for node in hiddenNodes:
         j += 1
         Edge(inputNode, node, i, j)
      
   #vytvori hrany medzi skrytou vrstvou a vystupom
   n_num += 1
   m = 0
   for node in hiddenNodes:
      m += 1
      Edge(node, outputNode, n_num, m)
  
   network.outputNode = outputNode
   network.inputNodes.extend(inputNodes)

   #data
   xorData = [
             ((0,0), 0),
             ((0,1), 1),
             ((1,0), 1),
             ((1,1), 0),
            ]

   network.train(xorData, float(learningRate), float(momentum), int(maxIterations))

   for number, result in xorData:
      print "Error for %r is %0.4f. Output was:%0.4f" % (number, result - network.evaluate(number, result, 4), network.evaluate(number, result, 4))

def parityRun(learningRate, momentum, maxIterations, inN, hN):

   n_num = int(inN)
   h_num = int(hN)
   network = Network()
   inputNodes = [InputNode(i) for i in range(int(n_num))]
   hiddenNodes = [Node() for i in range(int(h_num))]
   outputNode = Node()

   #drzat cislovanie hran - z akeho uzla ide , kam, vznikne tak pole - 
   #array zo suradnicami i, j - z iteho vstupu ide do jteho neuronu vyssej vrstvy

   # vytvori hrany medzi vstupnou vrstvou a skrytou vrstvou, vahy su random 
   i = 0
   
   for inputNode in inputNodes:
      i += 1
      j = 0
      for node in hiddenNodes:
         j += 1
         Edge(inputNode, node, i, j)
         #print InputNode
         #
         #print str(i) + "," + str(j)
         #print j

      #vytvori hrany medzi skrytou vrstvou a vystupom

   n_num += 1
   m = 0
   for node in hiddenNodes:
      m += 1
      Edge(node, outputNode, n_num, m)
      #print str(n_num) + "," + str(m)
      #print node

   network.outputNode = outputNode
   network.inputNodes.extend(inputNodes)

   ''' 
   result = []
   with open('parity.txt', 'r') as f:
     for line in f:
       result.extend(literal_eval(line.strip()))

   #print result
   parityData = result[:255]
   #print parityData
   ''' 
   new_inst = Data()
   parityData = new_inst.getData()
   network.train(parityData, float(learningRate), float(momentum), int(maxIterations))


   # test konzistentnosti
   #for number, isEven in parityData:
   #   print "Error for %r is %0.4f. Output was:%0.4f" % (number, isEven - network.evaluate(number), network.evaluate(number))

   
   #test input od pouzivatela
   #TODO - citat input z terminalu
   
   input_data = [((1,1,0,1,0,0,1,0), 0)]
   for number, result in input_data:
      #print number
      print "Input data: %r . Value needed: %0.4f - Output: %0.4f  " %  (number, result, network.evaluate(number, result, 256))
      
      #errors = abs(result - round(network.evaluate_test(number)))
      #print "Error: %0.4f" % (errors)
      #network.evaluate_test(number)


def sineTest(numLayers, numNodes):
   import math
   import random

   f = lambda x: 0.5 * (1.0 + math.sin(x))
   domain = lambda: [random.random()*math.pi*4 for _ in range(100)]

   network = makeNetwork(1, numLayers, numNodes)
   labeledExamples = [((x,), f(x)) for x in  domain()]
   network.train(labeledExamples, learningRate=0.25, maxIterations=100000)

   errors = [abs(f(x) - network.evaluate((x,))) for x in domain()]
   print "Avg error: %.4f" % (sum(errors) * 1.0 / len(errors))

   with open('sine.txt', 'a') as theFile:
      vals = tuple((x,network.evaluate((x,))) for x in domain())
      line = "{%s},\n" % (",".join(["{%s}" % ",".join([str(n) for n in x]) for x in vals]),)
      theFile.write(line)


def digitsTest():
   import random
   #network = makeNetwork(8, 1, 8)


   network = Network()
   inputNodes = [InputNode(i) for i in range(8)]
   hiddenNodes = [Node() for i in range(8)]
   outputNode = Node()

   # weights are all randomized
   for inputNode in inputNodes:
      for node in hiddenNodes:
         Edge(inputNode, node)


   for node in hiddenNodes:
      Edge(node, outputNode)

   network.outputNode = outputNode
   network.inputNodes.extend(inputNodes)

   digits = []
  

   ''' 
   with open('p_data.txt', 'r') as dataFile:
      for line in dataFile:
        #poriesit spracovanie \n na konci v premennej out_bin
        (inBin, outBin) = line.split('|') 
        digits.append(((inBin), outBin.rstrip()))  
        print inBin
        print outBin.rstrip()
        print digits
  '''
         

   with open('data_parity.txt', 'r') as dataFile:
      for line in dataFile:
         (exampleStr, classStr) = line.split(',')
         digits.append(([int(x) for x in exampleStr.split()], int(classStr)))
         #print exampleStr
         #print classStr
         #print digits

   
   #TODO define number of test and train data
   #random.shuffle(digits)
   trainingData = digits[-0:]
   #testData = digits[:-255]
   #testData = digits[-0:] 
   #print trainingData
   testData = [([1, 1, 1, 0, 0, 0, 0, 0], 1)]
   #print testData

   #testData = [((1,0,0,1,0,0,1,0), 1)]

   #network.train(trainingData, learningRate=0.8, momentum=0, maxIterations=1000)

   #input_data = [((1,0,0,1,0,0,1,0), 1)]
   #for number, result in input_data:
   #   print "Input data: %r . Value needed: %0.4f - Output: %0.4f  " %  (number, result, network.evaluate(trainingData), )
   errors = [abs(testPt[-1] - round(network.evaluate(testPt[0]))) for testPt in testData]

   print testData[0]
   print testPt[-1]
   print testPt[0]
   #print errors
   a = network.evaluate(testPt[0])
   print a

   #print "Average error: %.4f" % (sum(errors)*1.0 / len(errors))
   
   #print "Input: %0.4f - Output: %0.4f  " %  (testData[0], network.evaluate(testData[0]) )


if __name__ == "__main__":

   
   print "Do network:"

   n = len(sys.argv[1:])
   if n == 0:
     sys.exit('usage: python %s prameters' % sys.argv[0])
   elif sys.argv[1] == "xor":
     xorRun(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
   elif sys.argv[1] == "parity":
     parityRun(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

   
   #with open('data.txt','w') as theFile:
   #   theFile.write("{")

   #PARITY_test
   #parityRun()

   #with open('sine.txt','a') as theFile:
   #   theFile.write("}\n")

   #digitsTest()
   print('\a')
   print('\a')
   print('\a')
