import sys
sys.path.append(".")
import Bgate
import Tgate
import Gate
import Circuit

gateA = Bgate.Bgate('and', [1,0], 'gateA')
gateB = Bgate.Bgate('not', [1], 'gateB')
gateC = Bgate.Bgate('or', [gateA.output[0],gateB.output[0]], 'gateC')
gateSet = [gateA, gateB, gateC]


circuit1 = Circuit.Circuit("circuit1", gateSet)
circuit1.setEdge(gateA, gateB)
print(circuit1)


