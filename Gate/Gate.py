class Gate:

    def __init__(self, name, function, alphabet, k, l):
        self.name = name
        self.function = function
        self.alphabet = alphabet
        self.input_arity = k  # input arity
        self.output_arity = l  # output arity

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
        return self.input_arity
    
    def getL(self):
        return self.output_arity

    def evaluate(self, x):
        return self.function[(x)]

    def inverseGate(self, newName):
        """
            returns the inverse of the gate
        """
        if self.l != self.k:
            raise ValueError('Irreversible gate')
        #invfunction = self.function.invert()
        # need to build the invert dictionary somehow
        invfunction = []
        inv = Gate(newName, invfunction, self.alphabet, self.l, self.k)
        return inv


orGate =	{
  (0,0): 0,
  (0,1): 1,
  (1,0): 1,
  (1,1): 1,
  (0,0,0): (0,0,0),
  (0,1,0): (1,0,1),
  (1,0,0): (1,1,0),
  (1,1,0): (1,1,1),
  (0,0,1): (1,0,0),
  (0,1,1): (0,0,1),
  (1,0,1): (0,1,0),
  (1,1,1): (0,1,1)
}

andGate =   {
  (0,0): 0,
  (0,1): 0,
  (1,0): 0,
  (1,1): 1,
  (0,0,0): (0,0,0),
  (0,1,0): (0,0,1),
  (1,0,0): (0,1,0),
  (1,1,0): (1,1,1),
  (0,0,1): (1,0,0),
  (0,1,1): (1,0,1),
  (1,0,1): (1,1,0),
  (1,1,1): (0,1,1)
}

notGate =   {
  0: 1,
  1: 0,
  (0,0,0): (1,0,0),
  (0,1,0): (1,1,0),
  (1,0,0): (0,0,0),
  (1,1,0): (0,1,0),
  (0,0,1): (1,0,1),
  (0,1,1): (1,1,1),
  (1,0,1): (0,0,1),
  (1,1,1): (0,1,1)
}
"""
g = Gate(name="g", function=orGate, alphabet={0,1}, k=2, l=1)

x = (1,0)
print(g.evaluate(x))
"""

##################################################################
##################################################################
##################################################################

# Binary boolean gate class, a child of Gate representing an abstract BB gate,
# so alphabet is {0,1} and input is a tuple
class BBGate(Gate):

    def __init__(self, name, function, k):
        # Check if function is one of the valid BB gates
        if function not in [{(0,0): 0, (1,0): 0, (0,1): 0, (1,1): 1}, {(0,0): 0, (1,0): 1, (0,1): 1, (1,1): 1}, {0: 1, 1: 0}]:
            raise ValueError("Incorrect gate function")

        super(BBGate, self).__init__(name, function, {0,1}, k, 1)
    
# Binary boolean 'and' gate class, a child of BBGate representing an 'and' gate
class BBAndGate(BBGate):

    def __init__(self):
        super(BBAndGate, self).__init__('And', {(0,0): 0, (1,0): 0, (0,1): 0, (1,1): 1}, 2)

class BBOrGate(BBGate):

    def __init__(self):
        super(BBOrGate, self).__init__('Or', {(0,0): 0, (1,0): 1, (0,1): 1, (1,1): 1}, 2)

class BBNotGate(BBGate):

    def __init__(self):
        super(BBNotGate, self).__init__('Not', {0: 1, 1: 0}, 1)


g = BBAndGate()
x = (1,0)
print(g.evaluate(x))
y = (1,1)
print(g.evaluate(y))

g = BBOrGate()
x = (1,0)
print(g.evaluate(x))
y = (1,1)
print(g.evaluate(y))

g = BBNotGate()
x = 0
print(g.evaluate(x))


# Same stuff for ternary boolean gates, where alphabet is {0,1},
# and functions are on triples (and return triples)
class TBGate(Gate):

    def __init__(self, name, function):
        l = []
        for x in {0,1}:
            for y in {0,1}:
                for z in {0,1}:
                    l.append((x,y,z))
        a = {x: (((x[0] and x[1]) + x[2]) % 2, x[0], x[1]) for x in l}
        o = {x: (((x[0] or x[1]) + x[2]) % 2, x[0], x[1]) for x in l}
        n = {x: (1 - x[0], x[1], x[2]) for x in l}
        if function not in [a, o, n]:
            raise ValueError("Incorrect gate function")

        super(TBGate, self).__init__(name, function, {0,1}, 3, 3)

class TBAndGate(TBGate):

    def __init__(self):
        l = []
        for x in {0,1}:
            for y in {0,1}:
                for z in {0,1}:
                    l.append((x,y,z))
        f = {x: (((x[0] and x[1]) + x[2]) % 2, x[0], x[1]) for x in l}

        super(TBAndGate, self).__init__('And', f)

#g = TBAndGate()
#x = (1, 0, 0)
#print(g.evaluate(x))

# Example of bad BB gate attempt, get value error

#h = BBGate('bad', {0: 1}, 1)
#x = 0
#print(g.evaluate(x))