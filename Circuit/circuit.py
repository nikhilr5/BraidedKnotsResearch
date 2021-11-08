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

class Circuit:

    def __init__(self, name, gateSet):
        self.name = name
        self.constructGateDict(gateSet)

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

    def constructGateDict(self, gateSet):
        gateDict = {}
        for gate in gateSet:
            gateInputs = gate.input
            gateOutputs = gate.output
            currDict = {}
            currDict['input'] = gateInputs
            currDict['outputs'] = gateOutputs
            gateDict[gate.getName()] = currDict
        
        self.gateDict = gateDict
    
    def setEdge(gate1, gate2):
        gate1[].update({"color": "red"})
        gateDict[gate2.getName()].update("inputsEdge") = gate1.getName()




    
    