class Bgate:
    """
        I suppose we need a binary gate set
    """

    def __init__(self, gate_type, x, name):
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
        if len(x) != 2 or (x[0] != 0 and x[0] != 1) or (x[1] != 0 and x[1] != 1):
            raise ValueError('Invalid input')
        y = list();
        y.append(x[0] and x[1])
        self.output = y 

    def or_gate(self):
        x = self.input
        if len(x) != 2 or (x[0] != 0 and x[0] != 1) or (x[1] != 0 and x[1] != 1):
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

    def getName(self):
        return self.name