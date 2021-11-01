class Tgate:
    """
        Takes a binary gate and changes it to a reversible ternary gate.
    """
    
    
    def __init__(self, gate_type, x, name):
        """Initiates a new gate.
            Arguements: 
                - gate_type: the gate type
                - x: the binary set of bits
        """
        if len(x) > 2 or len(x) < 1:
            raise ValueError('Incorrect length of list')
        
        self.name = name
        self.input = x
        self.output = list();
        self.type = gate_type # gate_type = and/or/not
        
        if gate_type == 'and':
            self.and_gate(x)
        elif gate_type == 'or':
            self.or_gate(x)
        elif gate_type == 'not':
            self.not_gate(x)
        ## else, throw an exception
        else:
            raise ValueError('Incorrect gate type')
            
    def __str__(self):
        """
        Returns:
              Ternary gate.  
        """
        return f'{self.output}'
        
    def and_gate(self, x):
        """
        Arguement:
            A list with two bits that are being past into the 'AND' gate.
        Return: 
            Takes a binary 'AND' gate and returns a ternary gate.
            First bit is the output of the 'AND' gate of the two bits.
            Next two bits are the two bits.
        """
        y = list();
        y.append(((x[0] and x[1]) + 0) % 2)
        y.append(x[0])
        y.append(x[1])
        self.output = y 
    def or_gate(self, x):
        """
        Arguement:
            A list with two bits that are being past into the 'OR' gate.
        Return: 
            Takes a binary 'OR' gate and returns a ternary gate.
            First bit is the output of the 'OR' gate of the two bits.
            Next two bits are the two bits.
        """

        y = list();
        y.append(((x[0] or x[1]) + 0) % 2)
        y.append(x[0])
        y.append(x[1])
        self.output = y
    def not_gate(self, x):
        """
        Arguement:
            Takes in a list with one bit.
        Returns:
            A ternary gate.
            First bit is the NOT(x).
            Next two bits are ancillas.
        """
        y = list();
        if (len(x) != 1):
            raise ValueError('Length of list is incorrect.  The length must be equal to 1.')
            return
        if x[0] == 0:
            y.append(1)
        else:
            y.append(0)
        y.append(0)
        y.append(0)
        self.output = y

    def getName(self):
        return self.name