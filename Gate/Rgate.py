import sys
sys.path.append(".")
from Gate import Gate

class Rgate(Gate):
    """
    A class for reversible gates
    """
    #def __init__(self, name, function, alphabet, k, l):
    def __init__(self, name, function, alphabet, arity):
        """
        Initialization of a Bgate Object
        Arguments: 
            - gate_type: the gate type, a string 'and', 'or', or 'not'
            - x: a list of input bits, length should be 2 for 'and'/'or' gates and 1 for 'not' gates
            - name: a name
        """
        super().__init__(name, function, alphabet, arity, arity)

    def reverseGate(self, newName):
        """
            reverse the gate
        """
        #invfunction = self.function.invert()
        # need to build the invert dictionary somehow
        revfunction = dict(map(reversed, function.items()))
        rev = Gate(newName, revfunction, self.alphabet, self.arity)
        return rev

