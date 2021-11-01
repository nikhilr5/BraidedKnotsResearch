import sys
sys.path.append(".")
from Tgate import Tgate


####### Creates a gate object and takes a binary 'OR' gate with inputs [0,1]
####### Returns a ternary gate
orGate = Tgate('or',[0,1], 'gate1')
print("Ternary 'NOT' gate named ", orGate.getName(), " : ", orGate)

####### Creates a gate object and takes a binary 'AND' gate with inputs [0,1]
####### Returns a ternary gate
andGate = Tgate('and', [1,1], 'gate2')
print("Ternary 'NOT' gate named ", andGate.getName(), " : ", orGate)


####### Creates a gate object and takes a binary 'AND' gate with inputs [1]
####### Returns a ternary gate
notGate = Tgate('not', [1], 'gate3')
print("Ternary 'NOT' gate named ", notGate.getName(), " : ", notGate)