import random
import math


#
net = []
#net.insert(0, ((2,3),13))

def activationFunction(x):
   #sigmoid funkcia
   return 1.0 / (1.0 + math.exp(-x))

class Node:

   def __init__(self):
      self.lastOutput = None
      self.lastInput = None
      self.error = None
      self.outgoingEdges = []
      self.incomingEdges = []
      self.addBias()


   def addBias(self):
      self.incomingEdges.append(Edge(BiasNode(), self,0,0)) #chcecknut, ci netreba dat index_i, index_j

   def evaluate(self, inputVector, label, listLenght):
      if self.lastOutput is not None:
         return self.lastOutput

      self.lastInput = []
      weightedSum = 0
      sumMSE = 0
   

      #file = open("output.txt", "w")

      #print "*********************"
      for e in self.incomingEdges:
         theInput = e.source.evaluate(inputVector, label, listLenght)
         #print "Input:"
         #print theInput
         #print "["+ str(e.index_i) + "," + str(e.index_j) +"]" + " " + str(e.weight) 
         #table[e.index_i][e.index_j] = e.weight
         self.lastInput.append(theInput)
         weightedSum += e.weight * theInput  #TODO pridat prah
         #file.write(str(e.weight))
         #print "weight:"
         #print e.weight
         #print "--------------------"

      #file.close()
      


      self.lastOutput = activationFunction(weightedSum)
      self.evaluateCache = self.lastOutput
      #print "label:"
      #print label
      #print "result:"
      #print self.lastOutput
      #print "listLenght:"
      #print listLenght
      #sumMSE += ((label - self.lastOutput) ** 2)
      #print "sumMSE"
      #print sumMSE
      return self.lastOutput

   def evaluate_test(self, inputVector, result, listLenght):

      if self.lastOutput is not None:
         return self.lastOutput

      self.lastInput = []
      weightedSum = 0
   

      #file = open("output.txt", "w")

      #print "*********************"
      for e in self.incomingEdges:
         theInput = e.source.evaluate(inputVector, result. listLenght)
         #print "Input:"
         #print theInput
         #print "["+ str(e.index_i) + "," + str(e.index_j) +"]" + " " + str(e.weight)
         e.lastWeight = e.weight 
         #table[e.index_i][e.index_j] = e.weight

         net.insert(0, ((e.index_i,e,index_j),e.weight))

         self.lastInput.append(theInput)
         weightedSum += e.weight * theInput  #TODO pridat prah
         #file.write(str(e.weight))
         #print "weightedSum:"
         #print weightedSum
         #print "--------------------"
      

   def getError(self, label):

      '''Vrati error pre zadany uzol siete. 
         Ak je uzol vystupny, pre urcenie chyby pouzije vysledok zodpovedajuci vstupu. 
         Pri vstupnom uzle sa error neuvazuje  '''

      if self.error is not None:
         return self.error

      assert self.lastOutput is not None

      if self.outgoingEdges == []: # this is output node
         self.error = label - self.lastOutput
      else:
         self.error = sum([edge.weight * edge.target.getError(label) for edge in self.outgoingEdges])

      #print "Error:"   
      #print self.error
      return self.error

   def updateWeights(self, learningRate, momentum):
      
      '''Updatne vahy neuronu a nasledujucich. 
         Ak dojde k chybe, lastOutput a lastInput sa nastavia ako None a neuron bol updatnuty.
      '''

      if (self.error is not None and self.lastOutput is not None
            and self.lastInput is not None):

         for i, edge in enumerate(self.incomingEdges):
            edge.weight += (learningRate * self.lastOutput * (1 - self.lastOutput) *
                           self.error * self.lastInput[i])  + (momentum * edge.lastWeight)

         for edge in self.outgoingEdges:
            edge.target.updateWeights(learningRate, momentum)

         self.error = None
         self.lastInput = None
         self.lastOutput = None

   def clearEvaluateCache(self):
      if self.lastOutput is not None:
         self.lastOutput = None
         for edge in self.incomingEdges:
            edge.source.clearEvaluateCache()




class InputNode(Node):
   ''' 
    Vstupny uzol urci hodnotu pre zadany vstup podla prislusne zodpovedajuceho indexu. 
    '''

   def __init__(self, index):
      Node.__init__(self)
      self.index = index;

   def evaluate(self, inputVector, label, listLenght):
      self.lastOutput = inputVector[self.index]
      return self.lastOutput

   def evaluate_test(self, inputVector):
      self.lastOutput = inputVector[self.index]
      return self.lastOutput

   def updateWeights(self, learningRate, momentum):
      for edge in self.outgoingEdges:
         edge.target.updateWeights(learningRate, momentum)

   def getError(self, label):
      for edge in self.outgoingEdges:
         edge.target.getError(label)

   def addBias(self):
      pass

   def clearEvaluateCache(self):
      self.lastOutput = None


class BiasNode(InputNode):
   def __init__(self):
      Node.__init__(self)

   def evaluate(self, inputVector, label, listLenght):
      return 1.0


class Edge:
   def __init__(self, source, target, index_i, index_j):
      self.weight   = random.uniform(-0.5,0.5)
      self.source   = source
      self.target   = target
      self.lastWeight = 0
      self.index_i  = index_i
      self.index_j  = index_j
  
      # attach the edges to its nodes
      source.outgoingEdges.append(self)
      target.incomingEdges.append(self)


class Network:
   
   def __init__(self):
      self.inputNodes = []
      self.outputNode = None

   def evaluate(self, inputVector, result, listLenght):
      assert max([v.index for v in self.inputNodes]) < len(inputVector)
      self.outputNode.clearEvaluateCache()

      output = self.outputNode.evaluate(inputVector, result, listLenght)

      return output #vystup siete

   def evaluate_test(self, inputVector, result, listLenght):
      assert max([v.index for v in self.inputNodes]) < len(inputVector)
      self.outputNode.clearEvaluateCache()

      output = self.outputNode.evaluate_test(inputVector, result, listLenght)

      #MSE = ((result - output) ** 2) 
      #print "MSE:"
      #print MSE
      
      return output

   def getMSError(self, inputVector, result, listLenght):
      assert max([v.index for v in self.inputNodes]) < len(inputVector)
      self.outputNode.clearEvaluateCache()

      classifiedOK = 0

      output = self.outputNode.evaluate(inputVector, result, listLenght)
      '''
      print "Output: " + str(output)
      print "Result " + str(result)
      print "Diff: " + str(abs(output-result))
      '''
      dif = (output-result)
      if (math.fabs(dif) <= 0.3):
         classifiedOK += 1

      MSE = ((dif) ** 2) 

      return (MSE, classifiedOK)

   def propagateError(self, label):

      for node in self.inputNodes:
         nodeError = node.getError(label)
         #print "Node error"
         #print nodeError

      return nodeError   

   def updateWeights(self, learningRate, momentum):
      for node in self.inputNodes:
         node.updateWeights(learningRate, momentum)

   def train(self, labeledExamples, learningRate, momentum, maxIterations):
      

      #shuffle - bol problem s original shufflom (prevzata fcia)
      try:
      # available in Python 2.0 and later
         shuffle = random.shuffle
      except AttributeError:
         def shuffle(x):
            for i in xrange(len(x)-1, 0, -1):
            # pick an element in x[:i+1] with which to exchange x[i]
               j = int(random.random() * (i+1))
               x[i], x[j] = x[j], x[i]



      MSE = 0
      i=0

      while ((maxIterations > 0)): # and (MSE > 0.01)):
         MSE = 0
         classOK = 0
         i += 1
         shuffle(labeledExamples)
         for example, label in labeledExamples:
            #print example
            #print label
            output = self.evaluate(example, label, len(labeledExamples))
            getMSE, getClassifiedOK = self.getMSError(example, label, len(labeledExamples))  # TODO podla dlzky examplu
            #print getMSE
            #print getClassifiedOK
            MSE += getMSE
            classOK += getClassifiedOK

            #print output
            error = self.propagateError(label)
            #   
            #print "error:"
            # 
            #print error
            self.updateWeights(learningRate, momentum)
            #self.evaluate_test(example, label, len(labeledExamples))


            # TODO vysledky ciastkovych rozdielov pre kazdy z examplov
         #print "Len: " + str(len(labeledExamples))
         maxIterations -= 1
         
         #print MSE
         #print classOK
         MSE = MSE/len(labeledExamples)
         if((i % 10) == 1):
            print "Iteration: %d - MSE: %.4f - ClassifiedOK: %.4f " %  (i, MSE, float(classOK/len(labeledExamples)))
         #print "MSE_sum"
         #print MSE 

      # ulozenie natrenovanej siete 
      f = open('ulozenie_netrenov.txt','w')
      
      for iN in self.inputNodes:

         for e in iN.outgoingEdges:
            print "I: %d , J: %d" % (e.index_i, e.index_j)
            print "Weight: %0.4f" % e.weight
            net.insert(len(net),((e.index_i, e.index_j),e.weight))
            f.write(str(e.index_i))
            f.write(",")
            f.write(str(e.index_j))
            f.write("|")
            f.write(str(e.weight))
            f.write('\n')
            #f.write(str(((e.index_i, e.index_j),e.weight)))
            #f.write(",")

      for e in self.outputNode.incomingEdges:
         print "I: %d , J: %d" % (e.index_i, e.index_j)
         print "Weight: %0.4f" % e.weight
         net.insert(len(net),((e.index_i, e.index_j),e.weight))
         f.write(str(e.index_i))
         f.write(",")
         f.write(str(e.index_j))
         f.write("|")
         f.write(str(e.weight))
         f.write('\n')
         #f.write(str(((e.index_i, e.index_j),e.weight)))
         #f.write(",")
         # TODO - test, ci nerobi ciarka problem pri load dat

      print net
      
      f.close

      



   def runNet(self, labeledExamples, learningRate, momentum, maxIterations):
      for example, label in labeledExamples:
         print "Label: %d " % label
         print "Example: " + str(example)

         for aTuple in example:
            print(aTuple)
      
     


#print table
#print net
