import sys
sys.path.append(".")
import Tgate
from Gate import Gate

class Bgate(Gate):
    """
    I suppose we need a binary gate set (!?).
    """

    def __init__(self, gate_type, x, name):
        #super().__init__(name)
        self.input = x
        self.output = list()
        self.name = name
        self.type = gate_type

        if gate_type == 'and':
            self.and_gate()
        elif gate_type == 'or':
            self.or_gate()
        elif gate_type == 'not':
            self.not_gate()
        else:
            raise ValueError('Incorrect gate type')
    
    def and_gate(self):
        x = self.input
        # if len(x) != 2 or (x[0] != 0 and x[0] != 1) or (x[1] != 0 and x[1] != 1):
        #     raise ValueError('Invalid input')
        if not set(x).issubset({0,1}):
            raise ValueError('Invalid input')
        y = list();
        y.append(x[0] and x[1])
        self.output = y 

    def or_gate(self):
        x = self.input
        # if len(x) != 2 or (x[0] != 0 and x[0] != 1) or (x[1] != 0 and x[1] != 1):
        #     raise ValueError('Invalid input')
        if not set(x).issubset({0,1}):
            raise ValueError('Invalid input')
        y = list();
        y.append(x[0] or x[1])
        self.output = y 

    def not_gate(self):
        x = self.input
        if len(x) != 1 or (x[0] != 0 and x[0] != 1):
            raise ValueError('Invalid input')
        y = list();
        y.append(1 - x[0])
        self.output = y 

    def binary_to_ternary(self, ancilla, newName):
        """
        Take in a binary gate, return a corresponding ternary gate.
        """
        if self.type == 'and':
            x = list()
            x.append(self.input[0])
            x.append(self.input[1])
            x.append(ancilla)    # ancilla bit
            returnTGate = Tgate.Tgate('and', x, newName)
            return returnTGate
        if type == 'or':
            x = list()
            x.append(self.input[0])
            x.append(self.input[1])
            x.append(ancilla)    # ancilla bit
            returnTGate = Tgate.Tgate('or', x, newName)
            return returnTGate
        if type == 'not':
            x = list()
            x.append(self.input[0])
            x.append(0)     # ancilla
            x.append(0)     # ancilla 
            returnTGate = Tgate.Tgate('not', x, newName)
            return returnTGate

