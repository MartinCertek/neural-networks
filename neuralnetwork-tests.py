#from unittest import *
from neuralnetwork import *
from data import * 
from ast import literal_eval
import sys

net = []

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
         Edge(inputNode, node, i, j).weight
         
      
   #vytvori hrany medzi skrytou vrstvou a vystupom
   n_num += 1
   m = 0
   for node in hiddenNodes:
      m += 1
      Edge(node, outputNode, n_num, m).weight
  
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

   i = 0
   for inputNode in inputNodes:
      i += 1
      j = 0
      for node in hiddenNodes:
         j += 1
         print Edge(inputNode, node, i, j).weight
         e = Edge(inputNode, node, i, j).weight
         #f = Edge(inputNode, node, i, j).weight
         #print f
         net.insert(len(net), ((i,j),e))
         print Edge

         
      
   #vytvori hrany medzi skrytou vrstvou a vystupom
   n_num += 1
   m = 0
   for node in hiddenNodes:
      m += 1
      print Edge(node, outputNode, n_num, m).weight
      e = Edge(node, outputNode, n_num, m).weight
      #f = Edge(node, outputNode, n_num, m).weight
      #print f
      net.insert(len(net), ((n_num,m),e))


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
         

   #vytvori hrany medzi skrytou vrstvou a vystupom
   n_num += 1
   m = 0
   for node in hiddenNodes:
      m += 1
      Edge(node, outputNode, n_num, m)


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
   parityData = new_inst.getDataParity()
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


def telcoRun(learningRate, momentum, maxIterations, inN, hN):
   import random
   
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
         Edge(inputNode, node, i, j).weight
         
      
   #vytvori hrany medzi skrytou vrstvou a vystupom
   n_num += 1
   m = 0
   for node in hiddenNodes:
      m += 1
      Edge(node, outputNode, n_num, m).weight
  
   network.outputNode = outputNode
   network.inputNodes.extend(inputNodes)


   #nacitanie dat 
   new_inst = Data()
   telcoData = new_inst.getDataTelco()

   network.runNet(telcoData, learningRate, momentum, maxIterations)
   

   #TODO define number of test and train data
   #print "Lenght: %d " % len(telcoData)
   trainInxEnd = int(len(telcoData) * 0.01)
   testInxStr  = trainInxEnd
   #print "Test index: %d" % testInxStr

   trainingData = telcoData[-0:trainInxEnd]
   testData = telcoData[testInxStr:] 
   #print testData
   #testData = [([1, 1, 1, 0, 0, 0, 0, 0], 1)]
   #print testData

   # otvorenie suboru na zapis
   with open('telco_OUT.txt', 'w') as f:
      f.write(str(testData))
   


   network.train(trainingData, float(learningRate), float(momentum), int(maxIterations))

   #input_data = [((1,0,0,1,0,0,1,0), 1)]
   #for number, result in input_data:
   #   print "Input data: %r . Value needed: %0.4f - Output: %0.4f  " %  (number, result, network.evaluate(trainingData), )
   #errors = [abs(testPt[-1] - round(network.evaluate(testPt[0]))) for testPt in testData]
   '''
   print testData[0]
   print testPt[-1]
   print testPt[0]
   #print errors
   a = network.evaluate(testPt[0])
   print a
   '''
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
   elif sys.argv[1] == "telco":
     telcoRun(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

   
   #with open('data.txt','w') as theFile:
   #   theFile.write("{")

   #PARITY_test
   #parityRun()

   #with open('sine.txt','a') as theFile:
   #   theFile.write("}\n")

   #digitsTest()
   #print net

   

   print('\a')
   print('\a')
   print('\a')
