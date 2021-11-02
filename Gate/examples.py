import sys
sys.path.append(".")
import Bgate
import Tgate


####### Creates a Ternary gate object 'AND' gate with inputs [0,1,0]
####### Returns a ternary gate
#andGate = Tgate.Tgate('and',[0,1,0], 'gate1')
#print(andGate)

# ####### Creates a gate object and takes a binary 'AND' gate with inputs [0,1]
# ####### Returns a ternary gate
# andGate = Tgate('and', [1,1], 'gate2')
# print("Ternary 'NOT' gate named ", andGate.getName(), " : ", orGate)


# ####### Creates a gate object and takes a binary 'AND' gate with inputs [1]
# ####### Returns a ternary gate
# notGate = Tgate('not', [1], 'gate3')
# print("Ternary 'NOT' gate named ", notGate.getName(), " : ", notGate)

gate2 = Bgate.Bgate('and', [1,0], 'gate2')
print(gate2)

ternaryG = gate2.binary_to_ternary(0, 'coolGate')
#print(ternaryG)

gate3 = Tgate.Tgate('and', [1,0,0], 'gate3')
print(gate3)
