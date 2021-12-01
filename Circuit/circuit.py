###### DO SOMETHING COOL
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import Gate
import Bgate
import Tgate
from abc import abstractmethod
import copy
import networkx

class ReversibleCircuit:

    def __init__(self, name, gateList, input_arity, output_arity):
        """
            - gatelist: a list of tuples in the form (gate, idx1, idx2)
                where idx
        """
        self.name = name
        self.input_arity = input_arity
        self.output_arity = output_arity
        # throw an exception if input arity and output arity dont match
        self.gate_list = gateList
        #self.constructGateDict(gateSet)
        self.constructCircuit(gateList)


    def __str__(self):
        """
        Returns:
              - Gate set existing in circuit
              - All inputs
              - All outputs
        """
        return f' Gate Set: {self.gateDict}'

    def getName(self):
        return self.name

    def getGateDict(self):
        return self.getGateDict

    def constructCircuit(self, gateList):
        """
        wiring up the circuit
        later
        return the graph 
        """
        if len(gateList) == 0:
            return
        for (gate, idx1, idx2) in gateList:
            return
        #self.gateDict = gateDict
        return

    def evaluateCirtuit(self, x):
        """
            - x: input, a list of variables
            - output y, the circuit evaluated at input x
            the circuit is evaluated under the assumption that it is planar
        """
        gates = self.gate_list
        if len(gates) == 0:
            return x
        y = copy.deepcopy(x)  #output list
        for k in len(gates):
            gate, idx1, idx2 = gates[k]
            y[idx1, idx2 + 1] = gate.evaluate(y[idx1, idx2 + 1])
        return y

    def reverseCircuit(self, newName):
        revGateList = []
        gateList = self.gate_list
        n = len(gateList)
        for k in range(n):
            newGate = copy.deepcopy(gateList[n - 1 - k])
            newGate = newGate.reverseGate("inv"+newGate.name)
            revGateList.append(newGate)
        inv = ReversibleCircuit(newName, revGateList, self.output_arity, self.input_arity)
        return inv

        
    
    def setEdge(gate1, gate2):
        #gate1[].update({"color": "red"})
        #gateDict[gate2.getName()].update("inputsEdge") = gate1.getName()
        pass
