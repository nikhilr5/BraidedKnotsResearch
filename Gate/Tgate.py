import sys
sys.path.append(".")
import Bgate

class Tgate:
    """
    Takes a binary gate and changes it to a reversible ternary gate (better class description?).
    """
    
    def __init__(self, gate_type, x, name):
        """
        Initiates a new  ternary gate.
        Arguments: 
            - gate_type: the gate type, a string 'and', 'or', or 'not'
            - x: input bits, a set of length 3 consisting of 0, 1.
        Returns:
        """
        #super().__init__(name)
        #if len(x) > 2 or len(x) < 1:
        if len(x) != 3:
            raise ValueError('Incorrect length of input')
        # if (x[0] != 0 and x[0] != 1) or (x[1] != 0 and x[1] != 1) or (x[2] != 0 and x[2] != 1): # should find a way to make this line prettier 
        #     raise ValueError('Invalid input')
        if not set(x).issubset({0,1}):
            raise ValueError('Invalid input')
        self.name = name
        self.input = x
        self.output = list(); # ends up being set in the functions below anyways
        self.type = gate_type # gate_type = and/or/not
        if gate_type == 'and':
            self.and_gate()
        elif gate_type == 'or':
            self.or_gate()
        elif gate_type == 'not':
            self.not_gate()
        # else, throw an exception
        else:
            raise ValueError('Incorrect gate type')
            
    def __str__(self):
        """
        Returns:
            Ternary gate (in nice format?).
        """
        return f' Input of ternary gate: {self.input} \n Output of ternary gate: {self.output}'
        
    def and_gate(self):
        """
        Creates 'and' gate object.
        Arguments:
            None.
        Returns: 
            
        """
        x = self.input
        y = list();
        y.append(((x[0] and x[1]) + x[2]) % 2)
        y.append(x[0])
        y.append(x[1])
        self.output = y 

    def or_gate(self):
        """
        Creates 'or' gate object.
        Arguments:
            None.
        Returns: 
            
        """
        x = self.input
        y = list();
        y.append(((x[0] or x[1]) + x[2]) % 2)
        y.append(x[0])
        y.append(x[1])
        self.output = y

    def not_gate(self):
        """
        Creates 'not' gate object.
        Argument:
            None.
        Returns:
            Nothing, just set the output accordingly (this can be clearer).
        """
        x = self.input
        y = list();
        #if (len(x) != 1):
        #    raise ValueError('Length of list is incorrect.  The length must be equal to 1.')
        #    return
        if x[0] == 0:
            y.append(1)
        else:
            y.append(0)
        y.append(x[1])
        y.append(x[2])
        self.output = y

    def getName(self):
        return self.name

    def set_gate(self, new_gate):
        """
        A way to modify the gate type after initializing the gate 
        (works but doesn't look nice, can probably code it in a better way).
        Arguments:
            gate.
        Returns:
        """
        if new_gate != 'and' and new_gate != 'or' and new_gate != 'not':
            raise ValueError('Invalid gate type')
        tmpgate = Tgate(new_gate, self.input, self.name)
        self.input = tmpgate.input
        self.output = tmpgate.output
        self.type = tmpgate.type
        self.name = tmpgate.name

    # # Is this the function you want instead?
    # def set_gate1(self, new_gate_type)
    #     if new_gate_type not in ['and', 'or', 'not']:
    #         raise ValueError('Invalid gate type')
    #     tmpgate = Tgate(new_gate_type, self.input, self.name)
    #     self.input = tmpgate.input
    #     self.output = tmpgate.output
    #     self.type = tmpgate.type
    #     self.name = tmpgate.name

    def set_input(self, x):
        """
        A way to modify the input after initialization.
        Arguments:
        Returns:
        """
        if len(x) != 3:
            raise ValueError('Invalid input length')
        # if (x[0] != 0 and x[0] != 1) or (x[1] != 0 and x[1] != 1) or (x[2] != 0 and x[2] != 1):
        #     raise ValueError('Invalid input bits')
        if not set(x).issubset({0,1}):
            raise ValueError('Invalid input')
        tmpgate = Tgate(self.type, x, self.name)
        self.input = tmpgate.input
        self.output = tmpgate.output
        self.type = tmpgate.type
        self.name = tmpgate.name

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
