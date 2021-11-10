import sys
sys.path.append(".")
import Bgate
import Tgate

############### Creates Binary Gate
gate1 = Bgate.Bgate('and', [1,0], 'gate1')
print(gate1.getName(), '\n', gate1)

############# Takes the binary gate and ouputs a ternary gate
gate2 = gate1.binary_to_ternary(0, 'coolGate')
print(gate2.getName(), '\n', gate2)

############## Creates Ternary gate
gate3 = Tgate.Tgate('and', [1,0,0], 'gate3')
print(gate3.getName(), '\n', gate3)


