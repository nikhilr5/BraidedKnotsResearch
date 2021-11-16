import sys
sys.path.append(".")
import Bgate
from Gate import Gate

class Tgate(Gate):
    """
    Takes a binary gate and changes it to a reversible ternary gate (better class description?).
    """
    
    def __init__(self, function, name):
        """
        Initiates a new  ternary gate.
        Arguments: 
            - gate_type: the gate type, a string 'and', 'or', or 'not'
            - x: a list of input bits of length 3 consisting of 0, 1.
            - name: a name
        """
        # name function alphabet k l
        super().__init__(name, function, {0,1}, 3, 3)
        #if len(x) > 2 or len(x) < 1:
        #if len(x) != 3:
        #    raise ValueError('Incorrect length of input')
        #if not set(x).issubset({0,1}):
        #    raise ValueError('Invalid input')
        self.name = name
        #self.input = x
        #self.output = list(); # ends up being set in the functions below anyways
                            ## should still be a list unless you want to use ordered set
        self.function = function # gate_type = and/or/not
        if function == 'and':
            #self.and_gate()
            continue
        elif function == 'or':
            #self.or_gate()
            continue
        elif function == 'not':
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
        if len(x) != 3:
            raise ValueError('Incorrect length of input')
        y = list()
        if self.function == 'and':
            y = self.and_gate(x)
        elif self.function == 'or':
            y = self.or_gate(x)
        elif self.function == 'not':
            y = self.not_gate(x)
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
        if len(x) != 3:
            raise ValueError('Incorrect length of input')
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
        if len(x) != 3:
            raise ValueError('Incorrect length of input')
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
        if len(x) != 3:
            raise ValueError('Incorrect length of input')
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
    
