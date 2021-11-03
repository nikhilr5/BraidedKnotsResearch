from abc import abstractmethod

class Gate:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        """
        Returns:
              Ternary gate.  
        """
        return f' Input of Binary gate: {self.input} \n Ouput of binary gate: {self.output}'

    @abstractmethod
    def and_gate(self):
        pass

    @abstractmethod
    def or_gate(self):
        pass

    @abstractmethod
    def not_gate(self):
        pass

    def getName(self):
        return self.name
    
    