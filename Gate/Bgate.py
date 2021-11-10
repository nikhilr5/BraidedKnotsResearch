import sys
sys.path.append(".")
import Tgate
from Gate import Gate

class Bgate(Gate):
    """
    I suppose we need a binary gate set (!?).

    A class for the binary gates
    Each Bgate object consists of 3 main things: an input, a function, and an output
    and a name also
    """
    def __init__(self, function, name):
        """
        Initialization of a Bgate Object
        Arguments: 
            - gate_type: the gate type, a string 'and', 'or', or 'not'
            - x: a list of input bits, length should be 2 for 'and'/'or' gates and 1 for 'not' gates
            - name: a name
        """
        # name function alphabet k l
        #super().__init__(name, function, {0,1}, 2, 1)

        if function == 'and':
            super().__init__(name, function, {0,1}, 2, 1)
        elif function == 'or':
            super().__init__(name, function, {0,1}, 2, 1)
        elif function == 'not':
            super().__init__(name, function, {0,1}, 1, 1)
        else:
            raise ValueError('Incorrect gate type')
        self.name = name
        self.function = function
    
    def and_gate(self, x):
        if not len(x) != 2:
            raise ValueError('Invalid input length')
        if not set(x).issubset({0,1}):     # clever! nice & clean now
            raise ValueError('Invalid input')
        y = list()
        y.append(x[0] and x[1])
        self.output = y 

    def or_gate(self, x):
        if not len(x) != 2:
            raise ValueError('Invalid input length')
        if not set(x).issubset({0,1}):     # clever! nice & clean now
            raise ValueError('Invalid input')
        y = list()
        y.append(x[0] or x[1])
        self.output = y 

    def not_gate(self, x):
        if not len(x) != 1:
            raise ValueError('Invalid input length')
        if not set(x).issubset({0,1}):     # clever! nice & clean now
            raise ValueError('Invalid input')
        y = list()
        y.append(1 - x[0])
        self.output = y 
    

    def evaluate(self, x):
        """
        Arguments: 
            - x: input
        Output:
            - y: the gate function evaluated at x
        """
        if self.function == 'and':
            y = self.and_gate(x)
        elif self.function == 'or':
            y = self.or_gate(x)
        elif self.function == 'not':
            y = self.not_gate(x)
        else:
            raise ValueError('Incorrect gate type')
        return y


    def binary_to_ternary(self, newName):
        """
        Take in a binary gate, return a corresponding ternary gate.
        def __init__(self, gate_type, name) <- initialization of ternary gate
        """
        # name function alphabet k l
        if self.function == 'and':
            returnTGate = Tgate.Tgate('and', newName)
            return returnTGate
        if self.function == 'or':
            returnTGate = Tgate.Tgate('or', newName)
            return returnTGate
        if type == 'not':
            returnTGate = Tgate.Tgate('not', newName)
            return returnTGate

