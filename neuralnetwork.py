import random
import math

#natiahnut velkost zo vstupu
table= [ [ 0 for i in range(10) ] for j in range(10) ]
#print table

def activationFunction(x):
   #sigmoid function
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

   def evaluate(self, inputVector):
      if self.lastOutput is not None:
         return self.lastOutput

      self.lastInput = []
      weightedSum = 0
   

      #file = open("output.txt", "w")

      #print "*********************"
      for e in self.incomingEdges:
         theInput = e.source.evaluate(inputVector)
         print "Input:"
         print theInput
         print "["+ str(e.index_i) + "," + str(e.index_j) +"]" + " " + str(e.weight) 
         table[e.index_i][e.index_j] = e.weight
         self.lastInput.append(theInput)
         weightedSum += e.weight * theInput  #TODO pridat prah
         #file.write(str(e.weight))
         #print "weight:"
         #print e.weight
         #print "--------------------"

      #file.close()
      


      self.lastOutput = activationFunction(weightedSum)
      self.evaluateCache = self.lastOutput
      print "result:"
      print self.lastOutput
      return self.lastOutput

   def evaluate_test(self, inputVector):

      if self.lastOutput is not None:
         return self.lastOutput

      self.lastInput = []
      weightedSum = 0
   

      #file = open("output.txt", "w")

      #print "*********************"
      for e in self.incomingEdges:
         theInput = e.source.evaluate(inputVector)
         #print "Input:"
         #print theInput
         print "["+ str(e.index_i) + "," + str(e.index_j) +"]" + " " + str(e.weight)
         e.lastWeight = e.weight 
         table[e.index_i][e.index_j] = e.weight
         self.lastInput.append(theInput)
         weightedSum += e.weight * theInput  #TODO pridat prah
         #file.write(str(e.weight))
         print "weightedSum:"
         print weightedSum
         #print "--------------------"

   def getError(self, label):
      ''' Get the error for a given node in the network. If the node is an
         output node, label will be used to compute the error. For an input node, we
         simply ignore the error. '''

      if self.error is not None:
         return self.error

      assert self.lastOutput is not None

      if self.outgoingEdges == []: # this is output node
         self.error = label - self.lastOutput
      else:
         self.error = sum([edge.weight * edge.target.getError(label) for edge in self.outgoingEdges])
         #print edge.weight

      return self.error

   def updateWeights(self, learningRate, momentum):
      ''' Update the weights of a node, and all of its successor nodes.
         Assume self is not an InputNode. If the error, lastOutput, and
         lastInput are None, then this node has already been updated. '''

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
   ''' Input nodes simply evaluate to the value of the input for that index.
    As such, each input node must specify an index. We allow multiple copies
    of an input node with the same index (why not?). '''

   def __init__(self, index):
      Node.__init__(self)
      self.index = index;

   def evaluate(self, inputVector):
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

   def evaluate(self, inputVector):
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

   def evaluate(self, inputVector):
      assert max([v.index for v in self.inputNodes]) < len(inputVector)
      self.outputNode.clearEvaluateCache()

      output = self.outputNode.evaluate(inputVector)
      #print output
      return output

   def evaluate_test(self, inputVector):
      assert max([v.index for v in self.inputNodes]) < len(inputVector)
      self.outputNode.clearEvaluateCache()

      output = self.outputNode.evaluate_test(inputVector)
      #print output
      return output

   def propagateError(self, label):
      for node in self.inputNodes:
         node.getError(label)

   def updateWeights(self, learningRate, momentum):
      for node in self.inputNodes:
         node.updateWeights(learningRate, momentum)

   def train(self, labeledExamples, learningRate=0.9, momentum=0, maxIterations=100000):
      #random.shuffle(labeledExamples)
      #TODO add error rate as stop factor
      i =  range(len(labeledExamples))
      random.shuffle(i)
      print labeledExamples

      while maxIterations > 0:
         for example, label in labeledExamples:
            #print example
            #print label
            output = self.evaluate(example)
            #print output
            self.propagateError(label)
            self.updateWeights(learningRate, momentum)

            maxIterations -= 1

#print table
