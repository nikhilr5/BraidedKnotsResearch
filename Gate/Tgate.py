import sys
sys.path.append(".")
import Bgate
from Gate import Gate

class Tgate(Gate):
    """
    Takes a binary gate and changes it to a reversible ternary gate (better class description?).
    """
    
    def __init__(self, gate_type, name):
        """
        Initiates a new  ternary gate.
        Arguments: 
            - gate_type: the gate type, a string 'and', 'or', or 'not'
            - x: a list of input bits of length 3 consisting of 0, 1.
            - name: a name
        """
        super().__init__(name)
        #if len(x) > 2 or len(x) < 1:
        if len(x) != 3:
            raise ValueError('Incorrect length of input')
        #if not set(x).issubset({0,1}):
        #    raise ValueError('Invalid input')
        self.name = name
        #self.input = x
        #self.output = list(); # ends up being set in the functions below anyways
                            ## should still be a list unless you want to use ordered set
        self.type = gate_type # gate_type = and/or/not
        if gate_type == 'and':
            #self.and_gate()
            continue
        elif gate_type == 'or':
            #self.or_gate()
            continue
        elif gate_type == 'not':
            #self.not_gate()
            continue
        # else, throw an exception
    
    def evaluate(self, x):
        """
        Arguments: 
            - x: input
        Output:
            - y: the gate function evaluated at x
        """
        y = list()
        if gate_type == 'and':
            y = self.and_gate(x)
        elif gate_type == 'or':
            y = self.or_gate(x)
        elif gate_type == 'not':
            y = self.not_gate(x)
        # else, throw an exception
        else:
            raise ValueError('Incorrect gate type')
        return y
            
      
    def and_gate(self, x):
        """
        Evaluation
        Arguments:
            x
        Returns: 
            y
        """
        y = list()
        y.append(((x[0] and x[1]) + x[2]) % 2)
        y.append(x[0])
        y.append(x[1])
        return y 

    def or_gate(self, x):
        """
        Evaluation
        Arguments:
            x
        Returns: 
            y
        """
        y = list();
        y.append(((x[0] or x[1]) + x[2]) % 2)
        y.append(x[0])
        y.append(x[1])
        return y

    def not_gate(self, x):
        """
        Argument:
            x
        Returns:
            y
        """
        y = list();
        y.append(1-x[0])
        y.append(x[1])
        y.append(x[2])
        return y


    #def set_gate(self, new_gate):
        """
        A way to modify the gate type after initializing the gate 
        (works but doesn't look nice, can probably code it in a better way).
        Arguments:
            - new_gate: a string: 'and'/'or'/'not'
        Returns:
            None
        """
    #    if new_gate != 'and' and new_gate != 'or' and new_gate != 'not':
    #        raise ValueError('Invalid gate type')
    #    tmpgate = Tgate(new_gate, self.input, self.name)
    #    self.input = tmpgate.input
    #    self.output = tmpgate.output
    #    self.type = tmpgate.type
    #    self.name = tmpgate.name

    # # Is this the function you want instead?
    # def set_gate1(self, new_gate_type)
    #     if new_gate_type not in ['and', 'or', 'not']:
    #         raise ValueError('Invalid gate type')
    #     tmpgate = Tgate(new_gate_type, self.input, self.name)
    ## actually I was thinking about modifying the below chuck of code
    ## but they work, while simply setting self = tmpgate doesn't work
    #     self.input = tmpgate.input
    #     self.output = tmpgate.output
    #     self.type = tmpgate.type
    #     self.name = tmpgate.name

    #def set_input(self, x):
        """
        A way to modify the input after initialization.
        Arguments:
            - x: input, a list of length 3 
        Returns:
            None
        """
    #    if len(x) != 3:
    #        raise ValueError('Invalid input length')
    #    if not set(x).issubset({0,1}):
    #        raise ValueError('Invalid input')
    #    tmpgate = Tgate(self.type, x, self.name)
    #    self.input = tmpgate.input
    #    self.output = tmpgate.output
    #    self.type = tmpgate.type
    #    self.name = tmpgate.name
    

    # def binary_to_ternary(self, bgate, name, ancilla):
    #     # Take in a binary gate, return a corresponding ternary gate
    #     self.name = name
    #     self.type = bgate.type
    #     if self.type == 'and':
    #         x = list()
    #         x.append(bgate.input[0])
    #         x.append(bgate.input[1])
    #         x.append(ancilla)    # ancilla bit
    #         self.and_gate()
    #     if self.type == 'or':
    #         x = list()
    #         x.append(bgate.input[0])
    #         x.append(bgate.input[1])
    #         x.append(ancilla)    # ancilla bit
    #         self.or_gate()
    #     if self.type == 'not':
    #         x = list()
    #         x.append(bgate.input[0])
    #         x.append(0)     # ancilla
    #         x.append(0)     # ancilla 
    #         self.not_gate(ancilla)
