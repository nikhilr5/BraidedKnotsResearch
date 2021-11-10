class Gate:

    def __init__(self, name, function, alphabet, k, l):
        self.name = name
        self.function = function
        self.alphabet = alphabet
        self.k = k
        self.l = l

    def __str__(self):
        """
        Returns:
              Gate information
        """
        return f' Name: {self.name} \n Function: {self.function} \n Alphabet: {self.alphabet} \n k: {self.k} \n l: {self.l}'


    def getName(self):
        return self.name

    def getFunction(self):
        return self.function

    def getAlphabet(self):
        return self.alphabet
    
    def getK(self):
        return self.k
    
    def getL(self):
        return self.l

    def evaluate(self, x):
        return self.function[(x)]

    
orGate =	{
  (0,0): 0,
  (0,1): 1,
  (1,0): 2,
  (1,1): 3
}

g = Gate(name="g", function=orGate, alphabet={0,1}, k=2, l=1)

x = (1,0)
print(g.evaluate(x))

        


    