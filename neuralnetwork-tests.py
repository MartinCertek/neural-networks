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


   #ulozenie natrenovanych hodnot 
   n_num += 1
   m = 0
   for node in hiddenNodes:
      m += 1
      #print Edge(node, outputNode, n_num, m).weight
      e = Edge(node, outputNode, n_num, m).weight
      #f = Edge(node, outputNode, n_num, m).weight
      #print f
      net.insert(len(net), ((n_num,m),e))

   #shuffle premiesa hodnoty - znovuupratanie aby bol vystup prehladnejsi
   xorData = [
             ((0,0), 0),
             ((0,1), 1),
             ((1,0), 1),
             ((1,1), 0),
            ]

   print "\n"
   print "\n"
   print "\n"
   #test siete - vysledky, error
   for number, result in xorData:
      print "Error for %r is %0.4f. Output was:%0.4f" % (number, result - network.evaluate(number, result, 4), network.evaluate(number, result, 4))
         
      
 

# fcia na volanie behu parity - pracuje s parity datami
def parityRun(learningRate, momentum, maxIterations, inN, hN):

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


   #priradenie neuronov k sieti
   network.outputNode = outputNode
   network.inputNodes.extend(inputNodes)

   new_inst = Data()
   parityData = new_inst.getDataParity()
   network.train(parityData, float(learningRate), float(momentum), int(maxIterations))

   
   #test input od pouzivatela
   
   input_data = [((1,1,0,1,0,0,1,0), 0)]
   for number, result in input_data:
      #print number
      print "Input data: %r . Value needed: %0.4f - Output: %0.4f  " %  (number, result, network.evaluate(number, result, 256))
      



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

   
   #print "Lenght: %d " % len(telcoData)
   
   # trenovacie data = 20% vsetkych
   trainInxEnd = int(len(telcoData) * 0.2)
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

   test = telcoData[-0:1]

   network.runNet(test)

   #input_data = [((1,0,0,1,0,0,1,0), 1)]
   #for number, result in input_data:
   #   print "Input data: %r . Value needed: %0.4f - Output: %0.4f  " %  (number, result, network.evaluate(trainingData), )
   #errors = [abs(testPt[-1] - round(network.evaluate(testPt[0]))) for testPt in testData]
 
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


   

   print('\a')
   print('\a')
   print('\a')
